#!/usr/bin/env python
# main.py
# we use a Agent node, with RLChooseAction server and RLMemoryStore Subscriber, instead of a Process to train RL net.
# Before run this file, pleace do <rosrun robot_service RLAgent>


import numpy as np
from multiprocessing import Process, Lock, Pipe, Queue

import rospy, sys
from robot_service.msg import RLMemoryStore
from robot_service.srv import RLChooseAction
import os, time

# 设置全局变量
MAX_EPISODES = 4500
MAX_EP_STEPS = 50
MAX_STEP = MAX_EPISODES * MAX_EP_STEPS
ON_TRAIN = True  # True or False
LEARN_START = 25000
ALPHA = LEARN_START / MAX_EP_STEPS
BELTA = MAX_EPISODES - LEARN_START / MAX_EP_STEPS
VAR = 4  # control exploration
ACTION_NOISE = True

# 设置环境
name1 = 'worker1'
name2 = 'worker2'
seed1 = 5
seed2 = 10
s_dim = 23
a_dim = 9
a_bound = 1.


t1 = time.time()

# 开始训练

def train():
    
    worker1 = Process(target=train_loop, args=(seed1, name1))
    worker2 = Process(target=train_loop, args=(seed2, name2))

    worker1.start()
    worker2.start()

    worker1.join()
    worker2.join()

def train_loop(seed_set, name):
    
    print('%s initialing...' % name)
    from env_distri import mp500lwa4dEnv
    env = mp500lwa4dEnv(seed_set, name)

    fo = open(name+".txt", "w")
    # fo.close()
    # fo = open(name+".txt", "w")

    memory_store_pub = rospy.Publisher('/worker1/RLMemoryStore', RLMemoryStore, queue_size=10)
    RL_memory_data = RLMemoryStore()
    
    rospy.wait_for_service('RLChooseAction')
    try:
        RL_choose_action = rospy.ServiceProxy('RLChooseAction', RLChooseAction)
    except rospy.ServiceException.e:
        print( "Service call failed: %s" %e)
    print('%s initialization done' % name)
    # time_test1=time.clock()
    for i in range(MAX_EPISODES):

        s = env.reset()                # 初始化回合设置
        ep_r = 0.
        var = 0

        if ACTION_NOISE:
            if i <= LEARN_START / MAX_EP_STEPS:
                var = VAR
            elif i > LEARN_START / MAX_EP_STEPS and i <= (MAX_EPISODES - 250):

                var = (np.arctan((MAX_EPISODES / 2 - i)/400) / (np.pi / 2) + 1) * (VAR - 2)
            else:
                var = 0
        else:
            if i <= LEARN_START / MAX_EP_STEPS:
                var = VAR
            else:
                var = 0

        
        for j in range(MAX_EP_STEPS):         
            
            a = get_action(s, var, RL_choose_action)

            # print('%s| EPs: %i | Steps: %i |' %(name, i, j))        

            s_, r, done, info = env.step(a)   # 在环境中施加动作

            RL_memory_data.s = list(s)
            RL_memory_data.a = list(a)
            RL_memory_data.r = float(r)
            RL_memory_data.s_ = list(s_)
            memory_store_pub.publish(RL_memory_data)        # send data to memery
            
            ep_r += r
            s = s_                      # 变为下一回合
            if done or j == MAX_EP_STEPS - 1:
                print('Ep: %i | %s | ep_r1: %.1f | steps: %i' % (i, '---' if not done else 'done', ep_r, j))
                fo.write(str(i)+','+str(done)+','+str(ep_r)+','+str(j)+'\n')
                break
            # if j == 10:
            #     time_test2 = time.clock()
            #     print('used time: %.4f' %(time_test2 - time_test1))
    fo.close()
def get_action(s, var, RL_choose_action):

    choose_action_resp = RL_choose_action(list(s))
    a = np.array(choose_action_resp.action)
    # queue_action_req.put(s)
    # while True:
    #     if not queue_action_get.empty():
    #         a = queue_action_get.get()
    #         break
    a = np.clip(np.random.normal(a, var), -1, 1)
    a[2:8] = a[2:8] * np.pi/6
    a[1] = a[1] * np.pi
    return a

def eval():
    
    rl.restore()
    i = 0.0
    j = 0
    T = 0.0
    var = 0
    f = open('results.txt', 'a')
    while True:
        s = env.reset()
        ep_r = 0.
        i += 1
        for j in range(300):
            a = get_action(s, var)
            s, r, done, info = env.step(a)
            ep_r += r
            if done or j == 299:
                if done:
                    T += 1
                # else:
                #     for t in range(len(s)):
                #         f.write(str(s[t]))
                #         f.write(' ')
                #     f.write(str(env.goal['y']))
                #     f.write('\n')
                print(str(i)+','+str(done)+','+str(ep_r)+','+str(j)+'\n')
                break
        if i >= 5000:
            accuracy = T / i
            print("Steps accuracy: %f " % (accuracy))
            f.close()
            break

if __name__=='__main__':
    if ON_TRAIN:
        train()
    else:
        eval()
