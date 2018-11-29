#!/usr/bin/env python

import sent_velocity_client
import random
import globalvalue as gl
import sys
import rospy
import time
from math import pi
import numpy as np


def send_data():

    gl._init()

    linear_velocity = random.uniform(-1.5,1.5)
    angular_velocity = random.uniform(-2.4,2.4)

    base_1 = random.uniform(-pi/180,pi/180)
    arm1_2 = random.uniform(-pi/180,pi/180)
    arm2_3 = random.uniform(-pi/180,pi/180)
    arm3_4 = random.uniform(-pi/180,pi/180)
    arm4_5 = random.uniform(-pi/180,pi/180)
    arm5_6 = random.uniform(-pi/180,pi/180)
    arm6_7 = random.uniform(-pi/180,pi/180)

    gl.set_value('l_x', linear_velocity)
    gl.set_value('a_z', angular_velocity)
    gl.set_value('j_s_1', base_1)
    gl.set_value('j_s_2', arm1_2)
    gl.set_value('j_s_3', arm2_3)
    gl.set_value('j_s_4', arm3_4)
    gl.set_value('j_s_5', arm4_5)
    gl.set_value('j_s_6', arm5_6)
    gl.set_value('j_s_7', arm6_7)



def main():

    goal =eval(str(input('please input the goal coordinate: ')))
    list_x = list(goal)
    vector1 = list_x

    while not rospy.is_shutdown():
        send_data()
        sent_velocity_client.talker()
        sent_velocity_client.move_arm()

        #time.sleep(2)
        R_S = sent_velocity_client.ReadState()
        re_x, re_y, re_z = R_S.read_model_state()

        vector2 = np.array([re_x, re_y, re_z])
        op = np.linalg.norm(vector1 - vector2)
        reward = -1*op

        print('\n')
        print('The reward is :' + str(reward))
        print('\n')

if __name__ == "__main__" :

    main()




