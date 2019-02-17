#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rospy
import time
import math
from gazebo_msgs.srv import GetModelState
from gazebo_msgs.srv import GetLinkState
from gazebo_msgs.msg import LinkState
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Pose
from tf.transformations import euler_from_quaternion, quaternion_from_euler


class Stage:
    def __init__(self, linear = 0, angular = 0):
       self.linear  = linear
       self.angular = angular
       self.velocity_linear  = 0.5
       self.velocity_angular = 0.8
       self.duration1 = 0
       self.duration2 = 0    
    
    def get_duration(self):
        self.duration2 = abs(self.linear / self.velocity_linear)
        self.duration1 = abs(self.angular / self.velocity_angular)
    def vel_pub(self): #velocity publisher

        global pub_mobile, rate
        # while not rospy.is_shutdown():

        l_x = self.velocity_linear
        a_z = - self.velocity_angular
        if self.angular<=0:
            a_z = -a_z

        t_1 = rospy.get_time() #rotation
        rospy.sleep(0.01)
        t_2 = rospy.get_time()
        while t_2 - t_1 <= self.duration1 and not rospy.is_shutdown():
            la = Twist()
            la.linear.x = 0
            la.angular.z = a_z

            # rospy.loginfo(la)
            pub_mobile.publish(la)

            t_2 = rospy.get_time()

            
        print("finish rotation")
        rospy.sleep(1)
        t_1 = rospy.get_time() #transform
        rospy.sleep(0.01)
        t_2 = rospy.get_time()
        while t_2 - t_1 <= self.duration2 and not rospy.is_shutdown():
            la = Twist()
            la.linear.x = l_x
            la.angular.z = 0

            # rospy.loginfo(la)
            pub_mobile.publish(la)

            rate.sleep()
            t_2 = rospy.get_time()

            if t_2 - t_1 >= self.duration2 :
                break
            # break
        print("finish transform")
    
def relative_loc(pose_start,pose_end):
    PI          = 3.14159265
    stage1      = Stage()
    stage2      = Stage()
    stage3      = Stage()
    euler_start = [0, 0, 0]
    euler_end   = [0, 0, 0]
    q           = [0, 0, 0, 0]
    #print(pose_start.orientation)
    q[0]           = pose_start.orientation.x
    q[1]           = pose_start.orientation.y
    q[2]           = pose_start.orientation.z
    q[3]           = pose_start.orientation.w
    print("q is: " + str(q[0]) + str(q[1]) + str(q[2]) + str(q[3]))
    euler_start = euler_from_quaternion(q)

    q[0]           = pose_end.orientation.x
    q[1]           = pose_end.orientation.y
    q[2]           = pose_end.orientation.z
    q[3]           = pose_end.orientation.w
    euler_end   = euler_from_quaternion(q)
    rel_x       = pose_end.position.x - pose_start.position.x
    rel_y       = pose_end.position.y - pose_start.position.y
    rel_linear  = math.sqrt(rel_x**2 + rel_y**2)
    rel_angular = math.atan(rel_y/rel_x)
    if rel_x<=0:
        rel_angular -= PI
    
    # stage1.angular  = min(euler_start[2] - rel_angular, 2*PI - euler_start[2] + rel_angular)
    stage1.angular  = euler_start[2] - rel_angular
    stage1.get_duration()
    
    stage2.linear   = rel_linear
    stage2.get_duration()
    
    # stage3.angular  = min(rel_angular - euler_end[2], 2*PI - rel_angular + euler_end[2])
    stage3.angular  = rel_angular - euler_end[2]
    stage3.get_duration()

    return stage1, stage2, stage3

def read_model_state():

    try:
        resp_mobile = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        resp_arm = rospy.ServiceProxy('/gazebo/get_link_state', GetLinkState)
        resp_mobile_coordinates = resp_mobile('mp500lwa4d', 'world')


        print ('\n')
        print ('GetState success = ' + str(resp_mobile_coordinates.success))
        print('base')
        print('The pose relative to world :')
        print("position in x direction : " + str(resp_mobile_coordinates.pose.position.x))
        print("position in y direction : " + str(resp_mobile_coordinates.pose.position.y))
        print("position in z direction : " + str(resp_mobile_coordinates.pose.position.z))
        rospy.sleep(3)

        resp_arm_coordinates = resp_arm('arm_7_link', 'world')
        show_x = resp_arm_coordinates.link_state.pose.position.x
        show_y = resp_arm_coordinates.link_state.pose.position.y
        show_z = resp_arm_coordinates.link_state.pose.position.z

        # print('\n')
        # print('GetState success = ' + str(resp_arm_coordinates.success))
        # print('Endeffector')
        # print('The pose relative to world :')
        # print("position in x direction : " + str(resp_arm_coordinates.link_state.pose.position.x))
        # print("position in y direction : " + str(resp_arm_coordinates.link_state.pose.position.y))
        # print("position in z direction : " + str(resp_arm_coordinates.link_state.pose.position.z))

    except rospy.ServiceException as e:
        rospy.loginfo("Get Model State service call failed:  {0}".format(e))
    return resp_mobile_coordinates.pose


if __name__ == "__main__":
    
    pub_mobile = rospy.Publisher('/mp500lwa4d/mobile_base_controller/cmd_vel', Twist, queue_size=10)
    rospy.init_node('vel_pub', anonymous=False)
    rate = rospy.Rate(50)  # 50hz

    pose_start = Pose()
    pose_end   = Pose()

    pose_start = read_model_state()

    pose_end.position.x = 5
    pose_end.position.y = 0
    pose_end.position.z = pose_start.position.z

    quaternion = quaternion_from_euler(0, 0, 1.5707)
    pose_end.orientation.x = quaternion[0]
    pose_end.orientation.y = quaternion[1]
    pose_end.orientation.z = quaternion[2]
    pose_end.orientation.w = quaternion[3]
    count = 1
    while count<=1:
        stage1, stage2, stage3 = relative_loc(pose_start, pose_end)

        print ("stage1 angular is" + str(stage1.angular))
        print ("stage2 linear is" + str(stage2.linear))
        print ("stage3 angular is" + str(stage3.angular))

        print ("Begin stage1")
        stage1.vel_pub()
        print ("Finish stage1")
        print ("duration_rotation is " + str(stage1.duration1))
        print ("duration_transform is " + str(stage1.duration2))
        rospy.sleep(1)

        print ("Begin stage2")
        stage2.vel_pub()
        print ("Finish stage2")
        print ("stage2_transform is " + str(stage2.linear))
        print ("duration_rotation is " + str(stage2.duration1))
        print ("duration_transform is " + str(stage2.duration2))
        rospy.sleep(1)

        print ("Begin stage3")
        stage3.vel_pub()
        print ("Finish stage3")
        print ("duration_rotation is " + str(stage3.duration1))
        print ("duration_transform is " + str(stage3.duration2))
        rospy.sleep(1)

        count += 1
        pose_start = read_model_state()

    print('Target')
    print('The pose relative to world :')
    print("position in x direction : " + str(pose_end.position.x))
    print("position in y direction : " + str(pose_end.position.y))
    print("position in z direction : " + str(pose_end.position.z))
    print('Real')
    pose_real = read_model_state()
    print('Done')
    while(1):
        rospy.sleep(1)