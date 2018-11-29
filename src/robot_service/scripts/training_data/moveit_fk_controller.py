#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy, sys
import moveit_commander
from control_msgs.msg import GripperCommand

class MoveItFkDemo:
    def __init__(self, joint_positions):

        self.joint_positions = joint_positions
        # 初始化move_group的API
        moveit_commander.roscpp_initialize(sys.argv)

        # 初始化ROS节点
        rospy.init_node('moveit_fk_controller', anonymous=True)
 
        # 初始化需要使用move group控制的机械臂中的arm group
        self.arm = moveit_commander.MoveGroupCommander('arm')
        
        # 初始化需要使用move group控制的机械臂中的gripper group
        # gripper = moveit_commander.MoveGroupCommander('gripper')
        
        # 设置机械臂和夹爪的允许误差值
        self.arm.set_goal_joint_tolerance(0.001)
        # gripper.set_goal_joint_tolerance(0.001)
        
        # 控制机械臂先回到初始化位置
        self.arm.set_named_target('home')
        self.arm.go()
        rospy.sleep(10)
    def fk_move(self):
        # 设置夹爪的目标位置，并控制夹爪运动
        # gripper.set_joint_value_target([-0.04])
        # gripper.go()
        # rospy.sleep(5)
         
        # 设置机械臂的目标位置，使用六轴的位置数据进行描述（单位：弧度）
        self.arm.set_joint_value_target(self.joint_positions)
                 
        # 控制机械臂完成运动
        self.arm.go()
        rospy.sleep(1)
        
        # 关闭并退出moveit
        # moveit_commander.roscpp_shutdown()
        # moveit_commander.os._exit(0)

if __name__ == "__main__":
    try:
        joint_positions = [1, 1, 1, 1, 1, 1, 1]
        arm_joint = MoveItFkDemo(joint_positions)
        arm_joint.fk_move()
    except rospy.ROSInterruptException:
        pass