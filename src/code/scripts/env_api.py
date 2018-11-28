#!/usr/bin/env python

import random
import sys
import rospy
import time
from math import pi
import numpy as np
from MG_jointcontrol import MoveGroupPythonIntefaceTutorial
from gazebo_msgs.srv import GetModelState
from gazebo_msgs.srv import GetLinkState
from gazebo_msgs.msg import LinkState
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Pose

'''firstly you should define a goal position, either from your program or just input by keyboard, the goal position must be a 3-dimention corrdinate'''


class DRL_env(object):

    def __init__(self,goal):

        self.goal = goal


    def set_action(self):


        pub_mobile = rospy.Publisher('/mp500lwa4d/mobile_base_controller/cmd_vel', Twist, queue_size=10)
        rospy.init_node('set_action', anonymous=True)
        rate = rospy.Rate(10)  # 10hz
        move_arm = MoveGroupPythonIntefaceTutorial()

        la = Twist()
        la.linear.x = random.uniform(-1.0, 1.0)
        la.angular.z = random.uniform(-1.0, 1.0)
        rospy.loginfo(la)
        pub_mobile.publish(la)
        move_arm.go_to_joint_state()
        rate.sleep()

    def get_observation(self):

        try:
            resp_mobile = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
            resp_arm = rospy.ServiceProxy('/gazebo/get_link_state', GetLinkState)

            resp_mobile_coordinates = resp_mobile('mp500lwa4d', 'world')
            resp_arm_coordinates = resp_arm('arm_7_link', 'world')

            mobile_state = []

            mobile_p_x = resp_mobile_coordinates.pose.position.x
            mobile_p_y = resp_mobile_coordinates.pose.position.y
            mobile_p_z = resp_mobile_coordinates.pose.position.z

            mobile_v_x = resp_mobile_coordinates.twist.linear.x
            mobile_a_z = resp_mobile_coordinates.twist.angular.z

            mobile_state.append(mobile_p_x)
            mobile_state.append(mobile_p_y)
            mobile_state.append(mobile_p_z)
            mobile_state.append(mobile_v_x)
            mobile_state.append(mobile_a_z)


            print('\n')
            print('GetState success = ' + str(resp_mobile_coordinates.success))
            print('mp500lwa4d')
            print('The pose relative to world :')
            print("position in x direction : " + str(resp_mobile_coordinates.pose.position.x))
            print("position in y direction : " + str(resp_mobile_coordinates.pose.position.y))
            print("position in z direction : " + str(resp_mobile_coordinates.pose.position.z))

            arm_state = []

            arm_position_x = resp_arm_coordinates.link_state.pose.position.x
            arm_position_y = resp_arm_coordinates.link_state.pose.position.y
            arm_position_z = resp_arm_coordinates.link_state.pose.position.z

            arm_l_x = resp_arm_coordinates.link_state.twist.linear.x
            arm_l_y = resp_arm_coordinates.link_state.twist.linear.y
            arm_l_z = resp_arm_coordinates.link_state.twist.linear.z

            arm_a_x = resp_arm_coordinates.link_state.twist.angular.x
            arm_a_y = resp_arm_coordinates.link_state.twist.angular.y
            arm_a_z = resp_arm_coordinates.link_state.twist.angular.z

            arm_state.append(arm_position_x)
            arm_state.append(arm_position_y)
            arm_state.append(arm_position_z)
            arm_state.append(arm_l_x)
            arm_state.append(arm_l_y)
            arm_state.append(arm_l_z)
            arm_state.append(arm_a_x)
            arm_state.append(arm_a_y)
            arm_state.append(arm_a_z)

            print('\n')
            print('GetState success = ' + str(resp_arm_coordinates.success))
            print('Endeffector')
            print('The pose relative to world :')
            print("position in x direction : " + str(resp_arm_coordinates.link_state.pose.position.x))
            print("position in y direction : " + str(resp_arm_coordinates.link_state.pose.position.y))
            print("position in z direction : " + str(resp_arm_coordinates.link_state.pose.position.z))

        except rospy.ServiceException as e:
            rospy.loginfo("Get Model State service call failed:  {0}".format(e))
        return mobile_state, arm_state

    def get_reward(self):

        vector1 = self.goal
        mobile_state, arm_state = self.get_observation()
        vector2 = np.array([arm_state[0], arm_state[1], arm_state[2]])
        op = np.linalg.norm(vector1 - vector2)
        reward = -1 * op

        print('\n')
        print('The reward is :' + str(reward))
        print('\n')

        return reward


def main():

    robot_go = DRL_env([1,1,1])

    while not rospy.is_shutdown():
        robot_go.set_action()
        #robot_go.get_observation()
        reward = robot_go.get_reward()
        if reward >= -0.1:
             break

if __name__ == '__main__':

    main()



