#!/usr/bin/env python
import time
import math
from gym import logger

import gym
from gym import error, spaces
from gym.utils import seeding, closer

import rospy, sys
from control_msgs.msg import GripperCommand

from gazebo_msgs.srv import GetModelState
from gazebo_msgs.srv import GetLinkState
from gazebo_msgs.msg import LinkState, ModelState
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Pose

from tf.transformations import euler_from_quaternion, quaternion_from_euler

import pyglet
import numpy as np

MAX_EP_STEPS = 50
ARM_X_DOMAIN = 1.5  # 90.6
ARM_Y_DOMAIN = 1.5  # 90.6
X_DOMAIN = 4.4
Y_DOMAIN = 4.4


env_closer = closer.Closer()

# Env-related abstractions

class mp500lwa4dEnv(object):
    """The main OpenAI Gym class. It encapsulates an environment with
    arbitrary behind-the-scenes dynamics. An environment can be
    partially or fully observed.
    The main API methods that users of this class need to know are:
        step
        reset
        render
        close
        seed
    And set the following attributes:
        action_space: The Space object corresponding to valid actions
        observation_space: The Space object corresponding to valid observations
        reward_range: A tuple corresponding to the min and max possible rewards
    Note: a default reward range set to [-inf,+inf] already exists. Set it if you want a narrower range.
    The methods are accessed publicly as "step", "reset", etc.. The
    non-underscored versions are wrapper methods to which we may add
    functionality over time.
    """

    # Set this in SOME subclasses
    metadata = {'render.modes': []}
    reward_range = (-float('inf'), float('inf'))
    spec = None
    n_actions = 9

    # Set these in ALL subclasses
    action_space = spaces.Box(-1., 1., shape=(n_actions,), dtype='float32')
    observation_space = None

    action_bound = np.array([-1., 1.])
    action_arm_bound_pitch = action_bound * np.pi/2  # 转动的角度范围
    action_arm_bound_raw = action_bound * np.pi  # 转动的角度范围
    action_base_bound = action_bound * 2.5
    goal = {'x': 2.15, 'y': 2.675, 'l': 0.2}  # 蓝色 goal 的 x,y 坐标和长度 l
    # goal = {'x': 215., 'y': 267.5, 'l': 20}
    state_dim = 21  # 观测值
    action_dim = 9  # 动作
    s = np.zeros(state_dim)
    room_long = 2.5
    room_width = 2.5
    room_high = 2.5
    loc = [-2.5, 0.0, 2.5]
    loop = 0
    def __init__(self):
        # base velocity publisher
        self.pub_mobile = rospy.Publisher('/mp500lwa4d/mobile_base_controller/cmd_vel', Twist, queue_size=10)
        self.pub_arm1 = rospy.Publisher('/mp500lwa4d/arm_1_joint_position_controller/command', Float64, queue_size=10)
        self.pub_arm2 = rospy.Publisher('/mp500lwa4d/arm_2_joint_position_controller/command', Float64, queue_size=10)
        self.pub_arm3 = rospy.Publisher('/mp500lwa4d/arm_3_joint_position_controller/command', Float64, queue_size=10)
        self.pub_arm4 = rospy.Publisher('/mp500lwa4d/arm_4_joint_position_controller/command', Float64, queue_size=10)
        self.pub_arm5 = rospy.Publisher('/mp500lwa4d/arm_5_joint_position_controller/command', Float64, queue_size=10)
        self.pub_arm6 = rospy.Publisher('/mp500lwa4d/arm_6_joint_position_controller/command', Float64, queue_size=10)
        self.pub_arm7 = rospy.Publisher('/mp500lwa4d/arm_7_joint_position_controller/command', Float64, queue_size=10)

        self.pub_model_state = rospy.Publisher('/gazebo/set_model_state', ModelState, queue_size=10)
        
        rospy.init_node('robot_env', anonymous=False)
        rate = rospy.Rate(50)  # 50hz
        
        # arm position publisher
        # moveit_commander.roscpp_initialize(sys.argv)
        # rospy.init_node('moveit_fk_controller', anonymous=True)
        # self.arm = moveit_commander.MoveGroupCommander('arm')
        # self.arm.set_goal_joint_tolerance(0.001)
        # self.arm.set_joint_value_target([0, 0, 0, 0, 0, 0, 0])
        # self.arm.go()

        time.sleep(10)
    
        # init robot model state
        self.model_state_robot = ModelState()
        self.model_state_robot.model_name = 'mp500lwa4d'
        self.model_state_robot.pose.position.x = 0
        self.model_state_robot.pose.position.y = 0
        self.model_state_robot.pose.position.z = 0
        self.model_state_robot.pose.orientation.x = 0
        self.model_state_robot.pose.orientation.y = 0
        self.model_state_robot.pose.orientation.z = 0
        self.model_state_robot.pose.orientation.w = 0
        self.model_state_robot.reference_frame = 'world'
        self.pub_model_state.publish(self.model_state_robot)

        # init goal state
        self.model_state_goal = ModelState()
        self.model_state_goal.model_name = 'goal'
        self.model_state_goal.pose.position.x = 0
        self.model_state_goal.pose.position.y = 0
        self.model_state_goal.pose.position.z = 1
        self.model_state_goal.pose.orientation.x = 0
        self.model_state_goal.pose.orientation.y = 0
        self.model_state_goal.pose.orientation.z = 0
        self.model_state_goal.pose.orientation.w = 0
        self.model_state_goal.reference_frame = 'world'
        self.pub_model_state.publish(self.model_state_goal)
        
        self.base_vel = Twist()
        self.arm_joint_positions = [0, 0, 0, 0, 0, 0, 0]

        # init arm joints state
        self.pub_arm1.publish(self.arm_joint_positions[0])
        self.pub_arm2.publish(self.arm_joint_positions[1])
        self.pub_arm3.publish(self.arm_joint_positions[2])
        self.pub_arm4.publish(self.arm_joint_positions[3])
        self.pub_arm5.publish(self.arm_joint_positions[4])
        self.pub_arm6.publish(self.arm_joint_positions[5])
        self.pub_arm7.publish(self.arm_joint_positions[6])
        time.sleep(5)

  
        

        self.gripper_pose = Pose() 
        self.arm1_pose = [0, 0, 0]
        self.arm3_pose = [0, 0, 0]
        self.arm5_pose = [0, 0, 0]
        self.arm7_pose = [0, 0, 0]
        self.robot_orientation = [0, 0, 0, 0]
        self.robot_position = [0, 0, 0]
        self.dist_ = 0
        self.STU_FLAG = 0
        self.on_goal = 0
        self.t = 0

        # goal = {'x': 215., 'y': 267.5, 'z': 267.5, 'l': 20}

    def step(self, action):
        """Run one timestep of the environment's dynamics. When end of
        episode is reached, you are responsible for calling `reset()`
        to reset this environment's state.
        Accepts an action and returns a tuple (observation, reward, done, info).
        Args:
            action (object): an action provided by the environment
            action[0:2]=[base_vel_linear_x, base_vel_angular_z]
            action[2:9]=[arm1_angular,
                         arm2_angular,
                         arm3_angular,
                         arm4_angular,
                         arm5_angular,
                         arm6_angular,
                         arm7_angular,]
        Returns:
            observation (object): agent's observation of the current environment
            observation[0:7]=[arm1_angular,
                              arm2_angular,
                              arm3_angular,
                              arm4_angular,
                              arm5_angular,
                              arm6_angular,
                              arm7_angular,]
            observation[7:19]=[arm1_pose
                               arm3_pose
                               arm5_pose
                               arm7_pose]
            observation[19]  =[on_goal]
            reward (float) : amount of reward returned after previous action
            done (boolean): whether the episode has ended, in which case further step() calls will return undefined results
            info (dict): contains auxiliary diagnostic information (helpful for debugging, and sometimes learning)
        """
        done = False
        dt = 1 # time step equal to 1s
        info = {}
        r_angle = 0
        r_boundary = 0
        
        self.arm_joint_positions += action[2:9]

        self.arm_joint_positions[0] = np.clip(self.arm_joint_positions[0], *self.action_arm_bound_raw)
        self.arm_joint_positions[1] = np.clip(self.arm_joint_positions[1], *self.action_arm_bound_pitch)
        self.arm_joint_positions[2] = np.clip(self.arm_joint_positions[2], *self.action_arm_bound_raw)
        self.arm_joint_positions[3] = np.clip(self.arm_joint_positions[3], *self.action_arm_bound_pitch)
        self.arm_joint_positions[4] = np.clip(self.arm_joint_positions[4], *self.action_arm_bound_raw)
        self.arm_joint_positions[5] = np.clip(self.arm_joint_positions[5], *self.action_arm_bound_pitch)
        self.arm_joint_positions[6] = np.clip(self.arm_joint_positions[6], *self.action_arm_bound_raw)
        
        # publish arm joints position
        self.pub_arm1.publish(self.arm_joint_positions[0])
        self.pub_arm2.publish(self.arm_joint_positions[1])
        self.pub_arm3.publish(self.arm_joint_positions[2])
        self.pub_arm4.publish(self.arm_joint_positions[3])
        self.pub_arm5.publish(self.arm_joint_positions[4])
        self.pub_arm6.publish(self.arm_joint_positions[5])
        self.pub_arm7.publish(self.arm_joint_positions[6])
        time.sleep(2)
 
        # publish base velocity
        self.base_vel.linear.x = 0
        self.base_vel.angular.z = action[1]
        t_1 = time.clock()
        t_2 = time.clock()
        while t_2 - t_1 <= dt and not rospy.is_shutdown():
            self.pub_mobile.publish(self.base_vel) 
            t_2 = time.clock()

        self.base_vel.linear.x = action[0]
        self.base_vel.angular.z = 0
        t_1 = time.clock()
        t_2 = time.clock()
        while t_2 - t_1 <= dt and not rospy.is_shutdown():
            self.pub_mobile.publish(self.base_vel) 
            t_2 = time.clock()
        time.sleep(1)
        
        # get model state
        self.resp_robot_state, self.resp_arm1_coordinates,  self.resp_arm3_coordinates,  self.resp_arm5_coordinates,  self.resp_arm7_coordinates = self.read_model_state()
        self.robot_orientation[0]  =  self.resp_robot_state.pose.orientation.x
        self.robot_orientation[1]  =  self.resp_robot_state.pose.orientation.y
        self.robot_orientation[2]  =  self.resp_robot_state.pose.orientation.z
        self.robot_orientation[3]  =  self.resp_robot_state.pose.orientation.w

        # Loc_robot[0] = self.resp_robot_state.pose.position.x / (X_DOMAIN/2)
        # Loc_robot[1] = self.resp_robot_state.pose.position.y / (Y_DOMAIN/2)
        # if abs(Loc_robot[0]) <= 1: 
        #     if abs(Loc_robot[1]) <= 1:
        #         r_boundary = 0
        #     else:
        #         r_boundary = -1
        # else:
        #     r_boundary = -1

        self.arm1_pose = [self.resp_arm1_coordinates.link_state.pose.position.x, self.resp_arm1_coordinates.link_state.pose.position.y, self.resp_arm1_coordinates.link_state.pose.position.z]
        self.arm3_pose = [self.resp_arm3_coordinates.link_state.pose.position.x, self.resp_arm3_coordinates.link_state.pose.position.y, self.resp_arm3_coordinates.link_state.pose.position.z]
        self.arm5_pose = [self.resp_arm5_coordinates.link_state.pose.position.x, self.resp_arm5_coordinates.link_state.pose.position.y, self.resp_arm5_coordinates.link_state.pose.position.z]
        self.arm7_pose = [self.resp_arm7_coordinates.link_state.pose.position.x, self.resp_arm7_coordinates.link_state.pose.position.y, self.resp_arm7_coordinates.link_state.pose.position.z]

        finger = self.arm7_pose
#-------------- dist1 ------------------
        dist1 = [(self.goal['x'] - self.arm1_pose[0])/ self.room_long, (self.goal['y'] - self.arm1_pose[1])/ self.room_width, (self.goal['z'] - self.arm1_pose[2]) / self.room_high]
        # if abs(dist1[0]) <= ARM_X_DOMAIN:
        #     dist1[0] = dist1[0] / ARM_X_DOMAIN
        # else:
        #     dist1[0] = ((abs(dist1[0]) - ARM_X_DOMAIN) / (self.room_long - ARM_X_DOMAIN) + 1) * (dist1[0] / abs(dist1[0]))

        # if abs(dist1[1]) <= ARM_Y_DOMAIN:
        #     dist1[1] = dist1[1] / ARM_Y_DOMAIN
        # else:
        #     dist1[1] = ((abs(dist1[1]) - ARM_Y_DOMAIN) / (self.room_width - ARM_Y_DOMAIN) + 1) * (dist1[1] / abs(dist1[1]))
        dist1_ = np.sqrt(dist1[0] ** 2 + dist1[1] ** 2 + dist1[2] ** 2)
#-------------- dist2 -------------------
        dist2 = [(self.goal['x'] - self.arm3_pose[0])/ self.room_long, (self.goal['y'] - self.arm3_pose[1])/ self.room_width, (self.goal['z'] - self.arm3_pose[2]) / self.room_high]
        # if abs(dist2[0]) <= ARM_X_DOMAIN:
        #     dist2[0] = dist2[0] / ARM_X_DOMAIN
        # else:
        #     dist2[0] = ((abs(dist2[0]) - ARM_X_DOMAIN) / (self.room_long - ARM_X_DOMAIN) + 1) * (dist2[0] / abs(dist2[0]))

        # if abs(dist2[1]) <= ARM_Y_DOMAIN:
        #     dist2[1] = dist2[1] / ARM_Y_DOMAIN
        # else:
        #     dist2[1] = ((abs(dist2[1]) - ARM_Y_DOMAIN) / (self.room_width - ARM_Y_DOMAIN) + 1) * (dist2[1] / abs(dist2[1]))
#------------- dist3 ---------------------
        dist3 = [(self.goal['x'] - self.arm5_pose[0])/ self.room_long, (self.goal['y'] - self.arm5_pose[1])/ self.room_width, (self.goal['z'] - self.arm5_pose[2]) / self.room_high]
        # if abs(dist3[0]) <= ARM_X_DOMAIN:
        #     dist3[0] = dist3[0] / ARM_X_DOMAIN
        # else:
        #     dist3[0] = ((abs(dist3[0]) - ARM_X_DOMAIN) / (self.room_long - ARM_X_DOMAIN) + 1) * (dist3[0] / abs(dist3[0]))

        # if abs(dist3[1]) <= ARM_Y_DOMAIN:
        #     dist3[1] = dist3[1] / ARM_Y_DOMAIN
        # else:
        #     dist3[1] = ((abs(dist3[1]) - ARM_Y_DOMAIN) / (self.room_width - ARM_Y_DOMAIN) + 1) * (dist3[1] / abs(dist3[1]))
        dist3_ = np.sqrt(dist3[0] ** 2 + dist3[1] ** 2 + dist3[2] ** 2)
#------------- dist4 ---------------------
        dist4 = [(self.goal['x'] - finger[0])/ self.room_long, (self.goal['y'] - finger[1])/ self.room_width, (self.goal['z'] - finger[2]) / self.room_high]
        # if abs(dist4[0]) <= ARM_X_DOMAIN:
        #     dist4[0] = dist4[0] / ARM_X_DOMAIN
        # else:
        #     dist4[0] = ((abs(dist4[0]) - ARM_X_DOMAIN) / (self.room_long - ARM_X_DOMAIN) + 1) * (dist4[0] / abs(dist4[0]))

        # if abs(dist4[1]) <= ARM_Y_DOMAIN:
        #     dist4[1] = dist4[1] / ARM_Y_DOMAIN
        # else:
        #     dist4[1] = ((abs(dist4[1]) - ARM_Y_DOMAIN) / (self.room_width - ARM_Y_DOMAIN) + 1) * (dist4[1] / abs(dist4[1]))
        dist = np.sqrt(dist4[0] ** 2 + dist4[1] ** 2 + dist4[2] ** 2)
        # Reward
        r = (self.dist_ - dist) * 100
        # print ('dist_ is: %.3f | dist is: %.3f | r is: %.3f' % (self.dist_, dist, r))
        r += r_angle
        # r += r_boundary
        r -= 1 / MAX_EP_STEPS * 100

        self.dist_ = dist

        if dist3_ >= dist:
            r += 1.0
        # if dist1_ < self.radius:
        #     r += 0.004
        # 根据 finger 和 goal 的坐标得出 done and reward
        if self.goal['x'] - self.goal['l'] / 2 < finger[0] < self.goal['x'] + self.goal['l'] / 2:
            if self.goal['y'] - self.goal['l'] / 2 < finger[1] < self.goal['y'] + self.goal['l'] / 2:
                if self.goal['z'] - self.goal['l'] / 2 < finger[2] < self.goal['z'] + self.goal['l'] / 2:

                    # r = (self.dist_ - dist) * 10
                    self.on_goal += 1
                    if self.on_goal > 10:
                        done = True
                        r += 50 * self.on_goal

                        if self.goal['x'] - self.goal['l'] / 10 < finger[0] < self.goal['x'] + self.goal['l'] / 10:
                            if self.goal['y'] - self.goal['l'] / 10 < finger[1] < self.goal['y'] + self.goal['l'] / 10:
                                if self.goal['z'] - self.goal['l'] / 10 < finger[2] < self.goal['z'] + self.goal['l'] / 10:

                                    r += 1000
        else:
            self.on_goal = 0

        if np.sum(np.absolute(action)) <= 0.0001:
            self.STU_FLAG += 1
            if self.STU_FLAG >= 101:
                r -= 1 * self.STU_FLAG
        else:
            self.STU_FLAG = 0


        # state
        observation = np.concatenate((self.arm_joint_positions, self.robot_orientation, dist1, dist3, dist4, [1. if self.on_goal else 0.]))
        return observation, r, done, info

        # raise NotImplementedError

    def reset(self):
        """Resets the state of the environment and returns an initial observation.
        Returns: observation (object): the initial observation of the
            space.
        """
        if self.loop < 18:
            if self.loop < 6:
                self.goal['x'] = self.loc[0]
                self.goal['y'] = self.loc[self.loop % 3]
                if self.loop < 3:
                    self.goal['z'] = self.loc[1]
                else:
                    self.goal['z'] = self.loc[2]
            elif self.loop >= 12:
                self.goal['x'] = self.loc[2]
                self.goal['y'] = self.loc[self.loop % 3]
                if self.loop < 15:
                    self.goal['z'] = self.loc[1]
                else:
                    self.goal['z'] = self.loc[2]
            else:
                self.goal['x'] = self.loc[1]
                self.goal['y'] = self.loc[self.loop % 3]
                if self.loop < 9:
                    self.goal['z'] = self.loc[1]
                else:
                    self.goal['z'] = self.loc[2]
            
            self.arm_joint_positions = [0, 0, 0, 0, 0, 0, 0]
        else:
            self.goal['x'] = 0
            self.goal['y'] = 0
            self.goal['z'] = np.random.rand() * 2.50
            self.arm_joint_positions = (np.random.rand(7) - 0.5) * 2 * np.pi/2
            self.model_state_robot.pose.position.x = (np.random.rand() - 0.5) * X_DOMAIN 
            self.model_state_robot.pose.position.y = (np.random.rand() - 0.5) * Y_DOMAIN 
            self.model_state_robot.pose.position.z = 0
            quaternion = quaternion_from_euler(0, 0, (np.random.rand() - 0.5) * 2 * np.pi)
            self.model_state_robot.pose.orientation.x = quaternion[0]
            self.model_state_robot.pose.orientation.y = quaternion[1]
            self.model_state_robot.pose.orientation.z = quaternion[2]
            self.model_state_robot.pose.orientation.w = quaternion[3]
        
        self.loop += 1
        # goal_size = [0.1, 0.05, 0.05]
        # goal_pose = PoseStamped()
        # goal_pose.header.frame_id = REFERENCE_FRAME
        # goal_pose.pose.position.x = self.goal['x']
        # goal_pose.pose.position.y = self.goal['y']
        # goal_pose.pose.position.z = self.goal['z']
        # goal_pose.pose.orientation.w = 1.0   
        # scene.add_box(goal_id, goal_pose, goal_size)
        
        # reset model state
        self.pub_model_state.publish(self.model_state_robot)
        self.pub_arm1.publish(self.arm_joint_positions[0])
        self.pub_arm2.publish(self.arm_joint_positions[1])
        self.pub_arm3.publish(self.arm_joint_positions[2])
        self.pub_arm4.publish(self.arm_joint_positions[3])
        self.pub_arm5.publish(self.arm_joint_positions[4])
        self.pub_arm6.publish(self.arm_joint_positions[5])
        self.pub_arm7.publish(self.arm_joint_positions[6])

        self.model_state_goal = ModelState()
        self.model_state_goal.model_name = 'goal'
        self.model_state_goal.pose.position.x = self.goal['x']
        self.model_state_goal.pose.position.y = self.goal['y']
        self.model_state_goal.pose.position.z = self.goal['z']
        self.model_state_goal.reference_frame = 'world'
        self.pub_model_state.publish(self.model_state_goal)
        time.sleep(10)
        
        self.resp_robot_state, self.resp_arm1_coordinates,  self.resp_arm3_coordinates,  self.resp_arm5_coordinates,  self.resp_arm7_coordinates = self.read_model_state()
        self.robot_orientation[0]  =  self.resp_robot_state.pose.orientation.x
        self.robot_orientation[1]  =  self.resp_robot_state.pose.orientation.y
        self.robot_orientation[2]  =  self.resp_robot_state.pose.orientation.z
        self.robot_orientation[3]  =  self.resp_robot_state.pose.orientation.w
        # Loc_robot[0] = self.resp_robot_state.pose.position.x / (X_DOMAIN/2)
        # Loc_robot[1] = self.resp_robot_state.pose.position.y / (Y_DOMAIN/2)


        self.arm1_pose = [self.resp_arm1_coordinates.link_state.pose.position.x, self.resp_arm1_coordinates.link_state.pose.position.y, self.resp_arm1_coordinates.link_state.pose.position.z]
        self.arm3_pose = [self.resp_arm3_coordinates.link_state.pose.position.x, self.resp_arm3_coordinates.link_state.pose.position.y, self.resp_arm3_coordinates.link_state.pose.position.z]
        self.arm5_pose = [self.resp_arm5_coordinates.link_state.pose.position.x, self.resp_arm5_coordinates.link_state.pose.position.y, self.resp_arm5_coordinates.link_state.pose.position.z]
        self.arm7_pose = [self.resp_arm7_coordinates.link_state.pose.position.x, self.resp_arm7_coordinates.link_state.pose.position.y, self.resp_arm7_coordinates.link_state.pose.position.z]

        finger = self.arm7_pose
#-------------- dist1 ------------------
        dist1 = [(self.goal['x'] - self.arm1_pose[0])/ self.room_long, (self.goal['y'] - self.arm1_pose[1])/ self.room_width, (self.goal['z'] - self.arm1_pose[2]) / self.room_high]
        # if abs(dist1[0]) <= ARM_X_DOMAIN:
        #     dist1[0] = dist1[0] / ARM_X_DOMAIN
        # else:
        #     dist1[0] = ((abs(dist1[0]) - ARM_X_DOMAIN) / (self.room_long - ARM_X_DOMAIN) + 1) * (dist1[0] / abs(dist1[0]))

        # if abs(dist1[1]) <= ARM_Y_DOMAIN:
        #     dist1[1] = dist1[1] / ARM_Y_DOMAIN
        # else:
        #     dist1[1] = ((abs(dist1[1]) - ARM_Y_DOMAIN) / (self.room_width - ARM_Y_DOMAIN) + 1) * (dist1[1] / abs(dist1[1]))
        dist1_ = np.sqrt(dist1[0] ** 2 + dist1[1] ** 2 + dist1[2] ** 2)
#-------------- dist2 -------------------
        dist2 = [(self.goal['x'] - self.arm3_pose[0])/ self.room_long, (self.goal['y'] - self.arm3_pose[1])/ self.room_width, (self.goal['z'] - self.arm3_pose[2]) / self.room_high]
        # if abs(dist2[0]) <= ARM_X_DOMAIN:
        #     dist2[0] = dist2[0] / ARM_X_DOMAIN
        # else:
        #     dist2[0] = ((abs(dist2[0]) - ARM_X_DOMAIN) / (self.room_long - ARM_X_DOMAIN) + 1) * (dist2[0] / abs(dist2[0]))

        # if abs(dist2[1]) <= ARM_Y_DOMAIN:
        #     dist2[1] = dist2[1] / ARM_Y_DOMAIN
        # else:
        #     dist2[1] = ((abs(dist2[1]) - ARM_Y_DOMAIN) / (self.room_width - ARM_Y_DOMAIN) + 1) * (dist2[1] / abs(dist2[1]))
#------------- dist3 ---------------------
        dist3 = [(self.goal['x'] - self.arm5_pose[0])/ self.room_long, (self.goal['y'] - self.arm5_pose[1])/ self.room_width, (self.goal['z'] - self.arm5_pose[2]) / self.room_high]
        # if abs(dist3[0]) <= ARM_X_DOMAIN:
        #     dist3[0] = dist3[0] / ARM_X_DOMAIN
        # else:
        #     dist3[0] = ((abs(dist3[0]) - ARM_X_DOMAIN) / (self.room_long - ARM_X_DOMAIN) + 1) * (dist3[0] / abs(dist3[0]))

        # if abs(dist3[1]) <= ARM_Y_DOMAIN:
        #     dist3[1] = dist3[1] / ARM_Y_DOMAIN
        # else:
        #     dist3[1] = ((abs(dist3[1]) - ARM_Y_DOMAIN) / (self.room_width - ARM_Y_DOMAIN) + 1) * (dist3[1] / abs(dist3[1]))
        dist3_ = np.sqrt(dist3[0] ** 2 + dist3[1] ** 2 + dist3[2] ** 2)
#------------- dist4 ---------------------
        dist4 = [(self.goal['x'] - finger[0])/ self.room_long, (self.goal['y'] - finger[1])/ self.room_width, (self.goal['z'] - finger[2]) / self.room_high]
        # if abs(dist4[0]) <= ARM_X_DOMAIN:
        #     dist4[0] = dist4[0] / ARM_X_DOMAIN
        # else:
        #     dist4[0] = ((abs(dist4[0]) - ARM_X_DOMAIN) / (self.room_long - ARM_X_DOMAIN) + 1) * (dist4[0] / abs(dist4[0]))

        # if abs(dist4[1]) <= ARM_Y_DOMAIN:
        #     dist4[1] = dist4[1] / ARM_Y_DOMAIN
        # else:
        #     dist4[1] = ((abs(dist4[1]) - ARM_Y_DOMAIN) / (self.room_width - ARM_Y_DOMAIN) + 1) * (dist4[1] / abs(dist4[1]))
        dist = np.sqrt(dist4[0] ** 2 + dist4[1] ** 2 + dist4[2] ** 2)
        # Reward
        # r = (self.dist_ - dist) * 10
        # r += r_angle
        # r -= 1 / MAX_EP_STEPS * 10

        self.dist_ = dist

        # if dist3_ >= dist:
        #     r += 0.004
        # if dist1_ < self.radius:
        #     r += 0.004
        # 根据 finger 和 goal 的坐标得出 done and reward
        # if self.goal['x'] - self.goal['l'] / 2 < finger[0] < self.goal['x'] + self.goal['l'] / 2:
        #     if self.goal['y'] - self.goal['l'] / 2 < finger[1] < self.goal['y'] + self.goal['l'] / 2:
        #         if self.goal['z'] - self.goal['l'] / 2 < finger[2] < self.goal['z'] + self.goal['l'] / 2:

        #             # r = (self.dist_ - dist) * 10
        #             self.on_goal += 1
        #             if self.on_goal > 100:
        #                 done = True
        #                 r += 10 * self.on_goal

        #                 if self.goal['x'] - self.goal['l'] / 10 < finger[0] < self.goal['x'] + self.goal['l'] / 10:
        #                     if self.goal['y'] - self.goal['l'] / 10 < finger[1] < self.goal['y'] + self.goal['l'] / 10:
        #                         if self.goal['z'] - self.goal['l'] / 10 < finger[2] < self.goal['z'] + self.goal['l'] / 10:

        #                             r += 1000
        # else:
        #     self.on_goal = 0

        # if np.sum(np.absolute(action)) <= 0.0001:
        #     self.STU_FLAG += 1
        #     if self.STU_FLAG >= 101:
        #         r -= 1 * self.STU_FLAG
        # else:
        #     self.STU_FLAG = 0


        # state
        observation = np.concatenate((self.arm_joint_positions, self.robot_orientation, dist1, dist3, dist4, [1. if self.on_goal else 0.]))
        return observation
        # raise NotImplementedError

    def read_model_state(self):
        try:
            resp_mobile = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
            resp_arm = rospy.ServiceProxy('/gazebo/get_link_state', GetLinkState)
            resp_robot_state = resp_mobile('mp500lwa4d', 'world')
            resp_arm1_coordinates = resp_arm('arm_1_link', 'world')
            resp_arm3_coordinates = resp_arm('arm_3_link', 'world')
            resp_arm5_coordinates = resp_arm('arm_5_link', 'world')
            resp_arm7_coordinates = resp_arm('arm_7_link', 'world')

        except rospy.ServiceException as e:
            rospy.loginfo("Get Model State service call failed:  {0}".format(e))
        return resp_robot_state, resp_arm1_coordinates,  resp_arm3_coordinates,  resp_arm5_coordinates,  resp_arm7_coordinates

    def render(self, mode='human'):
        """Renders the environment.
        The set of supported modes varies per environment. (And some
        environments do not support rendering at all.) By convention,
        if mode is:
        - human: render to the current display or terminal and
          return nothing. Usually for human consumption.
        - rgb_array: Return an numpy.ndarray with shape (x, y, 3),
          representing RGB values for an x-by-y pixel image, suitable
          for turning into a video.
        - ansi: Return a string (str) or StringIO.StringIO containing a
          terminal-style text representation. The text can include newlines
          and ANSI escape sequences (e.g. for colors).
        Note:
            Make sure that your class's metadata 'render.modes' key includes
              the list of supported modes. It's recommended to call super()
              in implementations to use the functionality of this method.
        Args:
            mode (str): the mode to render with
            close (bool): close all open renderings
        Example:
        class MyEnv(Env):
            metadata = {'render.modes': ['human', 'rgb_array']}
            def render(self, mode='human'):
                if mode == 'rgb_array':
                    return np.array(...) # return RGB frame suitable for video
                elif mode is 'human':
                    ... # pop up a window and render
                else:
                    super(MyEnv, self).render(mode=mode) # just raise an exception
        """
        pass
        

    def close(self):
        """Override _close in your subclass to perform any necessary cleanup.
        Environments will automatically close() themselves when
        garbage collected or when the program exits.
        """
        return

    def seed(self, seed=None):
        """Sets the seed for this env's random number generator(s).
        Note:
            Some environments use multiple pseudorandom number generators.
            We want to capture all such seeds used in order to ensure that
            there aren't accidental correlations between multiple generators.
        Returns:
            list<bigint>: Returns the list of seeds used in this env's random
              number generators. The first value in the list should be the
              "main" seed, or the value which a reproducer should pass to
              'seed'. Often, the main seed equals the provided 'seed', but
              this won't be true if seed=None, for example.
        """
        # logger.warn("Could not seed environment %s", self)
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    @property
    def unwrapped(self):
        """Completely unwrap this env.
        Returns:
            gym.Env: The base non-wrapped gym.Env instance
        """
        return self

    def __str__(self):
        if self.spec is None:
            return '<{} instance>'.format(type(self).__name__)
        else:
            return '<{}<{}>>'.format(type(self).__name__, self.spec.id)


class GoalEnv(mp500lwa4dEnv):
    """A goal-based environment. It functions just as any regular OpenAI Gym environment but it
    imposes a required structure on the observation_space. More concretely, the observation
    space is required to contain at least three elements, namely `observation`, `desired_goal`, and
    `achieved_goal`. Here, `desired_goal` specifies the goal that the agent should attempt to achieve.
    `achieved_goal` is the goal that it currently achieved instead. `observation` contains the
    actual observations of the environment as per usual.
    """

    def reset(self):
        # Enforce that each GoalEnv uses a Goal-compatible observation space.
        if not isinstance(self.observation_space, gym.spaces.Dict):
            raise error.Error('GoalEnv requires an observation space of type gym.spaces.Dict')
        result = super(GoalEnv, self).reset()
        for key in ['observation', 'achieved_goal', 'desired_goal']:
            if key not in result:
                raise error.Error('GoalEnv requires the "{}" key to be part of the observation dictionary.'.format(key))
        return result

    def compute_reward(self, achieved_goal, desired_goal, info):
        """Compute the step reward. This externalizes the reward function and makes
        it dependent on an a desired goal and the one that was achieved. If you wish to include
        additional rewards that are independent of the goal, you can include the necessary values
        to derive it in info and compute it accordingly.
        Args:
            achieved_goal (object): the goal that was achieved during execution
            desired_goal (object): the desired goal that we asked the agent to attempt to achieve
            info (dict): an info dictionary with additional information
        Returns:
            float: The reward that corresponds to the provided achieved goal w.r.t. to the desired
            goal. Note that the following should always hold true:
                ob, reward, done, info = env.step()
                assert reward == env.compute_reward(ob['achieved_goal'], ob['goal'], info)
        """
        raise NotImplementedError()

# Space-related abstractions

class Space(object):
    """Defines the observation and action spaces, so you can write generic
    code that applies to any Env. For example, you can choose a random
    action.
    """
    def __init__(self, shape=None, dtype=None):
        import numpy as np # takes about 300-400ms to import, so we load lazily
        self.shape = None if shape is None else tuple(shape)
        self.dtype = None if dtype is None else np.dtype(dtype)

    def sample(self):
        """
        Uniformly randomly sample a random element of this space
        """
        raise NotImplementedError

    def contains(self, x):
        """
        Return boolean specifying if x is a valid
        member of this space
        """
        raise NotImplementedError

    __contains__ = contains

    def to_jsonable(self, sample_n):
        """Convert a batch of samples from this space to a JSONable data type."""
        # By default, assume identity is JSONable
        return sample_n

    def from_jsonable(self, sample_n):
        """Convert a JSONable data type to a batch of samples from this space."""
        # By default, assume identity is JSONable
        return sample_n


warn_once = True

def deprecated_warn_once(text):
    global warn_once
    if not warn_once: return
    warn_once = False
    logger.warn(text)


class Wrapper(mp500lwa4dEnv):
    env = None

    def __init__(self, env):
        self.env = env
        self.action_space = self.env.action_space
        self.observation_space = self.env.observation_space
        self.reward_range = self.env.reward_range
        self.metadata = self.env.metadata

    @classmethod
    def class_name(cls):
        return cls.__name__

    def step(self, action):
        if hasattr(self, "_step"):
            deprecated_warn_once("%s doesn't implement 'step' method, but it implements deprecated '_step' method." % type(self))
            self.step = self._step
            return self.step(action)
        else:
            deprecated_warn_once("%s doesn't implement 'step' method, " % type(self) +
                "which is required for wrappers derived directly from Wrapper. Deprecated default implementation is used.")
            return self.env.step(action)

    def reset(self, **kwargs):
        if hasattr(self, "_reset"):
            deprecated_warn_once("%s doesn't implement 'reset' method, but it implements deprecated '_reset' method." % type(self))
            self.reset = self._reset
            return self._reset(**kwargs)
        else:
            deprecated_warn_once("%s doesn't implement 'reset' method, " % type(self) +
                "which is required for wrappers derived directly from Wrapper. Deprecated default implementation is used.")
            return self.env.reset(**kwargs)

    def render(self, mode='human', **kwargs):
        return self.env.render(mode, **kwargs)

    def close(self):
        if self.env:
            return self.env.close()

    def seed(self, seed=None):
        return self.env.seed(seed)

    def compute_reward(self, achieved_goal, desired_goal, info):
        return self.env.compute_reward(achieved_goal, desired_goal, info)

    def __str__(self):
        return '<{}{}>'.format(type(self).__name__, self.env)

    def __repr__(self):
        return str(self)

    @property
    def unwrapped(self):
        return self.env.unwrapped

    @property
    def spec(self):
        return self.env.spec


class ObservationWrapper(Wrapper):
    def step(self, action):
        observation, reward, done, info = self.env.step(action)
        return self.observation(observation), reward, done, info

    def reset(self, **kwargs):
        observation = self.env.reset(**kwargs)
        return self.observation(observation)

    def observation(self, observation):
        deprecated_warn_once("%s doesn't implement 'observation' method. Maybe it implements deprecated '_observation' method." % type(self))
        return self._observation(observation)


class RewardWrapper(Wrapper):
    def reset(self):
        return self.env.reset()

    def step(self, action):
        observation, reward, done, info = self.env.step(action)
        return observation, self.reward(reward), done, info

    def reward(self, reward):
        deprecated_warn_once("%s doesn't implement 'reward' method. Maybe it implements deprecated '_reward' method." % type(self))
        return self._reward(reward)


class ActionWrapper(Wrapper):
    def step(self, action):
        action = self.action(action)
        return self.env.step(action)

    def reset(self):
        return self.env.reset()

    def action(self, action):
        deprecated_warn_once("%s doesn't implement 'action' method. Maybe it implements deprecated '_action' method." % type(self))
        return self._action(action)

    def reverse_action(self, action):
        deprecated_warn_once("%s doesn't implement 'reverse_action' method. Maybe it implements deprecated '_reverse_action' method." % type(self))
        return self._reverse_action(action)