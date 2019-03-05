#!/usr/bin/env python
from DDPG_dropout_small_net import DDPG  #_dropout
import numpy as np
import os, time
import rospy, sys
from robot_service.msg import RLMemoryStore
from robot_service.srv import RLChooseAction, RLChooseActionResponse
from multiprocessing import Process
import threading

s_dim = 23
a_dim = 9
a_bound = 1.
ACTION_NOISE = True
MAX_EPISODES = 4000
MAX_EP_STEPS = 50
MAX_STEP = MAX_EPISODES * MAX_EP_STEPS * 2
LEARN_START = 25000
store_steps = 0
learn_steps = 0
reason = 'Learning completed'




rl = DDPG(a_dim, s_dim, a_bound, ACTION_NOISE)  # Agent





def RLchoose_action(req):
    global store_steps
    global learn_steps
    global rl
    action = list(rl.choose_action(np.array(req.state)))
    if store_steps >= LEARN_START:
        learn_steps += 1
        for i in range(10):
            rl.learn()
    if store_steps >= MAX_STEP:
        rospy.signal_shutdown(reason)
    return RLChooseActionResponse(action)

def RLmemory_store(data):
    global store_steps
    global rl
    store_steps += 1
    s = list(data.s)
    a = list(data.a)
    r = float(data.r)
    s_ = list(data.s_)
    rl.store_transition(s, a, r, s_)
    rospy.loginfo( "store memory %i" %store_steps)
    if store_steps >= MAX_STEP:
        rospy.signal_shutdown(reason)

def RL_choose_action_server():
    choose_action = rospy.Service('RLChooseAction', RLChooseAction, RLchoose_action)
    while not rospy.is_shutdown():
        rospy.rostime.wallsleep(0.5)

def RL_memory_store_node():
    memory = rospy.Subscriber("/worker1/RLMemoryStore", RLMemoryStore, RLmemory_store)
    while not rospy.is_shutdown():
        rospy.rostime.wallsleep(0.5)



if __name__ == "__main__":
    rospy.init_node('RLAgent', anonymous=True, disable_signals=True)
    RL_choose_action = threading.Thread(target=RL_choose_action_server, args=())
    RL_memory_store = threading.Thread(target=RL_memory_store_node, args=())

    RL_choose_action.start()
    RL_memory_store.start()

    RL_choose_action.join()
    RL_memory_store.join()
    
    rl.save()
    print( "Agent Save successfully, Learned %i times." %(learn_steps*10))