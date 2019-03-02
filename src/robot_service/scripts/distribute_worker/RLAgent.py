#!/usr/bin/env python
from DDPG_dropout_small_net import DDPG  #_dropout
import numpy as np
import os, time
import rospy, sys
from robot_service.msg import RLMemoryStore
from robot_service.srv import RLChooseAction, RLChooseActionResponse

s_dim = 23
a_dim = 9
a_bound = 1.
ACTION_NOISE = True




rl = DDPG(a_dim, s_dim, a_bound, ACTION_NOISE)  # Agent





def RLchoose_action(req):
    action = list(rl.choose_action(np.array(req.state)))
    return RLChooseActionResponse(action)

def RLmemory_store(data):
    s = list(data.s)
    a = list(data.a)
    r = float(data.r)
    s_ = list(data.s_)
    rl.store_transition(s, a, r, s_)
    rl.learn()

def RL_choose_action_server():  
    choose_action = rospy.Service('RLChooseAction', RLChooseAction, RLchoose_action)
    rospy.spin()

def RL_memory_store_node():
    
    memory = rospy.Subscriber("RLMemoryStore", RLMemoryStore, RLmemory_store)
    rospy.spin()



if __name__ == "__main__":
    rospy.init_node('RLAgent', anonymous=True)
    RL_choose_action_server()
    RL_memory_store_node()

        