"""
Note: This is a updated version from my previous code,
for the target network, I use moving average to soft replace target parameters instead using assign function.
By doing this, it has 20% speed up on my machine (CPU).
Deep Deterministic Policy Gradient (DDPG), Reinforcement Learning.
DDPG is Actor Critic based algorithm.
Pendulum example.
View more on my tutorial page: https://morvanzhou.github.io/tutorials/
Using:
tensorflow 1.0
gym 0.8.0
"""

import tensorflow as tf
import numpy as np
from Noise import AdaptiveParamNoiseSpec
from copy import copy
# import gym
# import time


#####################  hyper parameters  ####################

LR_A = 0.001    # learning rate for actor
LR_C = 0.002    # learning rate for critic
GAMMA = 0.9     # reward discount
TAU = 0.01      # soft replacement
MEMORY_CAPACITY = 5000000
BATCH_SIZE = 512
STDDEV = 0.1



###############################  DDPG  ####################################


class DDPG(object):
    def __init__(self, a_dim, s_dim, a_bound, ACTION_NOISE):
        self.memory = np.zeros((MEMORY_CAPACITY, s_dim * 2 + a_dim + 1), dtype=np.float32)
        self.pointer = 0
        self.sess = tf.Session()
        self.noise = AdaptiveParamNoiseSpec()
        self.ACTION_NOISE = ACTION_NOISE

        self.a_dim, self.s_dim, self.a_bound = a_dim, s_dim, a_bound,
        self.S = tf.placeholder(tf.float32, [None, s_dim], 's')
        self.S_ = tf.placeholder(tf.float32, [None, s_dim], 's_')
        self.R = tf.placeholder(tf.float32, [None, 1], 'r')
        self.param_noise_stddev = tf.placeholder(tf.float32, shape=(), name='param_noise_stddev')
        self.a_params = tf.placeholder(tf.float32, shape=(), name='a_params')
        self.tf_is_training = tf.placeholder(tf.bool, None)  # to control dropout when training and testing

        self.a = self._build_a(self.S,)
        q = self._build_c(self.S, self.a, )
        self.a_params = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope='Actor')
        c_params = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, scope='Critic')
        ema = tf.train.ExponentialMovingAverage(decay=1 - TAU)          # soft replacement

        def ema_getter(getter, name, *args, **kwargs):
            return ema.average(getter(name, *args, **kwargs))

        target_update = [ema.apply(self.a_params), ema.apply(c_params)]      # soft update operation
        a_ = self._build_a(self.S_, reuse=True, custom_getter=ema_getter)   # replaced target parameters
        q_ = self._build_c(self.S_, a_, reuse=True, custom_getter=ema_getter)

        a_loss = - tf.reduce_mean(q)  # maximize the q

        self.atrain = tf.train.AdamOptimizer(LR_A).minimize(a_loss, var_list=self.a_params)

        with tf.control_dependencies(target_update):    # soft replacement happened at here
            q_target = self.R + GAMMA * q_
            td_error = tf.losses.mean_squared_error(labels=q_target, predictions=q)
            self.ctrain = tf.train.AdamOptimizer(LR_C).minimize(td_error, var_list=c_params)

        self.sess.run(tf.global_variables_initializer())

    def choose_action(self, s):
        return self.sess.run(self.a, {self.S: s[np.newaxis, :], self.tf_is_training: False})[0]

    def learn(self):
        if self.pointer < MEMORY_CAPACITY:
            indices = np.random.choice(self.pointer, size=BATCH_SIZE)
        else:
            indices = np.random.choice(MEMORY_CAPACITY, size=BATCH_SIZE)
        bt = self.memory[indices, :]
        bs = bt[:, :self.s_dim]
        ba = bt[:, self.s_dim: self.s_dim + self.a_dim]
        br = bt[:, -self.s_dim - 1: -self.s_dim]
        bs_ = bt[:, -self.s_dim:]

        if not self.ACTION_NOISE:
            perturbed_params = copy(self.a_params)
            a_params_perturbed = get_perturbed_actor_updates(self.a_params, perturbed_params, self.param_noise_stddev)  # self.noise.current_stddev)  # New
            # if self.a_params is not a_params_perturbed:
            self.a_params = a_params_perturbed
                # print("add noise to a_paramerters")

        self.sess.run(self.atrain, {self.S: bs, self.tf_is_training: True})
        self.sess.run(self.ctrain, {self.S: bs, self.a: ba, self.R: br, self.S_: bs_, self.tf_is_training: True})

        # adaptive_actor_tf = np.random.normal(self.actor, self.noise.current_stddev)
        # if self.noise is not None:
        #     self.adaptive_policy_distance = tf.sqrt(tf.reduce_mean(tf.square(self.actor_tf - adaptive_actor_tf)))
        #     distance = self.sess.run(self.adaptive_policy_distance, )
        #     self.noise.adapt(distance)

    def store_transition(self, s, a, r, s_):
        transition = np.hstack((s, a, [r], s_))
        if self.pointer < MEMORY_CAPACITY:
            index = self.pointer
        else:
            index = self.pointer % MEMORY_CAPACITY
            # if self.pointer < MEMORY_CAPACITY * 3 / 2:
            #     index = self.pointer % MEMORY_CAPACITY + 5000000  # replace the old memory with new memory
            # else:
            #     index = self.pointer % int(MEMORY_CAPACITY * 3 / 2) + 5000000
        self.memory[index, :] = transition
        self.pointer += 1

    def _build_a(self, s, reuse=None, custom_getter=None):
        trainable = True if reuse is None else False
        with tf.variable_scope('Actor', reuse=reuse, custom_getter=custom_getter):
            net1 = tf.layers.dense(s, 128, activation=tf.nn.relu, name='l1', trainable=trainable)
            net2 = tf.layers.dense(net1, 256, activation=tf.nn.relu, name='l2', trainable=trainable)
            net2 = tf.layers.dropout(net2, rate=0.5, training=self.tf_is_training)
            # net3 = tf.layers.dense(net2, 512, activation=tf.nn.relu, name='l3', trainable=trainable)
            a = tf.layers.dense(net2, self.a_dim, activation=tf.nn.tanh, name='a', trainable=trainable)
            return tf.multiply(a, self.a_bound, name='scaled_a')

    def _build_c(self, s, a, reuse=None, custom_getter=None):
        trainable = True if reuse is None else False
        with tf.variable_scope('Critic', reuse=reuse, custom_getter=custom_getter):
            n_l1 = 100
            w1_s = tf.get_variable('w1_s', [self.s_dim, n_l1], trainable=trainable)
            w1_a = tf.get_variable('w1_a', [self.a_dim, n_l1], trainable=trainable)
            b1 = tf.get_variable('b1', [1, n_l1], trainable=trainable)
            net = tf.nn.relu(tf.matmul(s, w1_s) + tf.matmul(a, w1_a) + b1)
            return tf.layers.dense(net, 1, trainable=trainable)  # Q(s,a)

    def save(self):
        saver = tf.train.Saver()
        saver.save(self.sess, './params', write_meta_graph=False)

    def restore(self):
        saver = tf.train.Saver()
        saver.restore(self.sess, './params')


def get_perturbed_actor_updates(a_params, perturbed_actor, param_noise_stddev):
    updates = []

    for var, perturbed_var in zip(a_params, perturbed_actor):
        tf.assign(perturbed_var, var + tf.random_normal(tf.shape(var), mean=0., stddev=param_noise_stddev))
        updates.append(perturbed_var)

    return updates


