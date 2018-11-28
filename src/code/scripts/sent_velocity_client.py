#!/usr/bin/env python

import sys
import rospy
import time
import globalvalue as gl
from MG_jointcontrol import MoveGroupPythonIntefaceTutorial
from gazebo_msgs.srv import GetModelState
from gazebo_msgs.srv import GetLinkState
from gazebo_msgs.msg import LinkState
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Pose


class ReadState:


    def read_model_state(self):

        try:
            resp_mobile = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
            resp_arm = rospy.ServiceProxy('/gazebo/get_link_state', GetLinkState)
            resp_mobile_coordinates = resp_mobile('mp500lwa4d', 'world')

            print ('\n')
            print ('GetState success = ' + str(resp_mobile_coordinates.success))
            print('mp500lwa4d')
            print('The pose relative to world :')
            print("position in x direction : " + str(resp_mobile_coordinates.pose.position.x))
            print("position in y direction : " + str(resp_mobile_coordinates.pose.position.y))
            print("position in z direction : " + str(resp_mobile_coordinates.pose.position.z))

            resp_arm_coordinates = resp_arm('arm_7_link', 'world')
            show_x = resp_arm_coordinates.link_state.pose.position.x
            show_y = resp_arm_coordinates.link_state.pose.position.y
            show_z = resp_arm_coordinates.link_state.pose.position.z

            print('\n')
            print('GetState success = ' + str(resp_arm_coordinates.success))
            print('Endeffector')
            print('The pose relative to world :')
            print("position in x direction : " + str(resp_arm_coordinates.link_state.pose.position.x))
            print("position in y direction : " + str(resp_arm_coordinates.link_state.pose.position.y))
            print("position in z direction : " + str(resp_arm_coordinates.link_state.pose.position.z))

        except rospy.ServiceException as e:
            rospy.loginfo("Get Model State service call failed:  {0}".format(e))
        return show_x, show_y, show_z




def talker():

    pub_mobile = rospy.Publisher('/mp500lwa4d/mobile_base_controller/cmd_vel', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz

    while not rospy.is_shutdown():

        l_x = gl.get_value('l_x')
        a_z = gl.get_value('a_z')
        t_1 = rospy.get_time()

        while not rospy.is_shutdown():

            la = Twist()
            la.linear.x = l_x
            la.angular.z = a_z

            rospy.loginfo(la)
            pub_mobile.publish(la)

            rate.sleep()
            t_2 = rospy.get_time()

            if t_2 - t_1 >= 1 :

                break
        break

def move_arm():

    tutorial = MoveGroupPythonIntefaceTutorial()
    tutorial.go_to_joint_state()


def main():

    while not rospy.is_shutdown():

        talker()
        move_arm()

        time.sleep(2)
        R_S = ReadState()
        R_S.read_model_state()

if __name__ == "__main__":

    main()

