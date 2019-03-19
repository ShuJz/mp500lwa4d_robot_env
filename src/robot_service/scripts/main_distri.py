#!/usr/bin/env python
# main.py
# 导入环境和学习方法


import numpy as np
from multiprocessing import Process, Lock, Pipe, Queue
import os, time

# 设置全局变量
MAX_EPISODES = 2000
MAX_EP_STEPS = 50
MAX_STEP = MAX_EPISODES * MAX_EP_STEPS - 1000
ON_TRAIN = True  # True or False
LEARN_START = 2500
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
    
    queue_worker1_action_req = Queue()
    queue_worker2_action_req = Queue()
    queue_worker1_action_get = Queue()
    queue_worker2_action_get = Queue()

    queue_state = Queue()

    agent = Process(target=agent_loop, args=(queue_worker1_action_req, queue_worker2_action_req, queue_worker1_action_get, queue_worker2_action_get, queue_state))
    worker1 = Process(target=train_loop, args=(seed1, name1, queue_worker1_action_req, queue_worker1_action_get, queue_state))
    worker2 = Process(target=train_loop, args=(seed2, name2, queue_worker2_action_req, queue_worker2_action_get, queue_state))

    agent.start()
    worker1.start()
    worker2.start()

    agent.join()
    worker1.join()
    worker2.join()

def train_loop(seed_set, name, queue_action_req, queue_action_get, queue_state):
    
    from env_distri import mp500lwa4dEnv
    env = mp500lwa4dEnv(seed_set, name)

    time_test1=time.clock()
    for i in range(MAX_EPISODES):

        s = env.reset()                # 初始化回合设置
        ep_r = 0.
        var = 0

        if ACTION_NOISE:
            if i <= LEARN_START / MAX_EP_STEPS:
                var = VAR
            elif i > LEARN_START / MAX_EP_STEPS and i <= (MAX_EPISODES - 100):

                var = (np.arctan((MAX_EPISODES / 2 - i)/200) / (np.pi / 2) + 1) * (VAR - 2)
            else:
                var = 0
        else:
            if i <= LEARN_START / MAX_EP_STEPS:
                var = VAR
            else:
                var = 0

        
        for j in range(MAX_EP_STEPS):         
            
            a = get_action(s, var, queue_action_req, queue_action_get)

            print('%s| EPs: %i | Steps: %i |' %(name, i, j))        

            s_, r, done, info = env.step(a)   # 在环境中施加动作
            
            if queue_state.empty():           # send data to memery
                queue_state.put((s, a, r, s_))
            
            ep_r += r
            s = s_                      # 变为下一回合
            if done or j == MAX_EP_STEPS - 1:
                print('Ep: %i | %s | ep_r1: %.1f | steps: %i' % (i, '---' if not done else 'done', ep_r, j))
                break
            if j == 10:
                time_test2 = time.clock()
                print('used time: %.4f' %(time_test2 - time_test1))

        
        
        # if i == 5999 or i == 7999:
        #     rl.save()
    # rl.save()

def agent_loop(queue_work1_req, queue_work2_req, queue_work1_get, queue_work2_get, queue_state):

    from DDPG_dropout_small_net import DDPG  #_dropout
    rl = DDPG(a_dim, s_dim, a_bound, ACTION_NOISE)  # Agent
    i = 0
    j = 0
    while True:
        if not queue_work1_req.empty():
            queue_work1_get.put(rl.choose_action(queue_work1_req.get())) # RL 选择动作
        if not queue_work2_req.empty():
            queue_work2_get.put(rl.choose_action(queue_work2_req.get()))
        if not queue_state.empty():
            s, a, r, s_ = queue_state.get()
            rl.store_transition(s, a, r, s_)  # DDPG 这种强化学习需要存放记忆库
            i += 1
            # print('total steps: %i' %(i))
            if i >= LEARN_START:
                # print('Learn')
                rl.learn() 
                j += 1
                if (j%1000) == 0:
                    print ('Agent has learned %i times' %j)    
        if i >= MAX_STEP:
               rl.save() 



def get_action(s, var, queue_action_req, queue_action_get):

    queue_action_req.put(s)
    while True:
        if not queue_action_get.empty():
            a = queue_action_get.get()
            break
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
                print('Ep: %i | %s | ep_r: %.1f | steps: %i' % (i, '---' if not done else 'done', ep_r, j))
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
