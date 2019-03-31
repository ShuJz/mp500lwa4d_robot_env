import pyglet
import numpy as np

MAX_EP_STEPS = 500
MAX_EPISODES = 40000
LEARN_START = 5000000
ALPHA = LEARN_START / MAX_EP_STEPS
BELTA = MAX_EPISODES - LEARN_START / MAX_EP_STEPS
ARM_X_DOMAIN = 100  # 90.6
ARM_Y_DOMAIN = 100  # 90.6
X_DOMAIN = 200
Y_DOMAIN = 200


class mlRoboEnv(object):

    viewer = None  # 首先没有 viewer

    dt = 0.1  # 转动的速度和 dt 有关
    action_bound = np.array([-1., 1.])
    action_arm_bound = action_bound * np.pi/2  # 转动的角度范围
    action_base_bound = action_bound * 170 + 200
    goal = {'x': 215., 'y': 267.5, 'l': 25}  # 蓝色 goal 的 x,y 坐标和长度 l
    # goal = {'x': 215., 'y': 267.5, 'l': 20}
    state_dim = 9  # 观测值
    action_dim = 4  # 动作
    s = np.zeros(state_dim)

    def __init__(self):
        self.arm_info = np.zeros(
            4, dtype=[('l', np.float32)])
        self.arm_angle_info = np.ones(3) * np.pi / 6 # 手臂的端点角度
        # 生成出 (2,4) 的矩阵
        self.arm_info['l'][0] = 36.2  # 手臂1 36.2 长
        self.arm_info['l'][1] = 32.5
        self.arm_info['l'][2] = 32.5
        self.arm_info['l'][3] = 25.6
        self.radius = self.arm_info['l'][1] + self.arm_info['l'][2] + self.arm_info['l'][3]
        self.base_loc = np.array([200, 200], dtype=np.float)
        self.STU_FLAG = 0
        self.on_goal = 0
        self.dist_ = 0
        self.t = 0

    def step(self, action):
        action_arm = action[0:3]
        action_base = action[3]
        done = False
        r_angle = 0
        info = {}

        # 计算单位时间 dt 内旋转的角度, 将角度限制在+(-)180度以内
        self.base_loc[0] += action_base * self.dt
        self.base_loc[0] = np.clip(self.base_loc[0], *self.action_base_bound)

        self.arm_angle_info += action_arm * self.dt
        a2r_ = np.abs(self.arm_angle_info[0])
        a3r_ = np.abs(self.arm_angle_info[1])
        a4r_ = np.abs(self.arm_angle_info[2])
        # reward come from arm angle
        if a2r_ > (9 * np.pi / 20):
            r_angle -= a2r_ / (np.pi / 2) * 0.5
        if a3r_ > (9 * np.pi / 20):
            r_angle -= a3r_ / (np.pi / 2) * 0.5
        if a4r_ > (9 * np.pi / 20):
            r_angle -= a4r_ / (np.pi / 2) * 0.5

        self.arm_angle_info[0] = np.clip(self.arm_angle_info[0], *self.action_arm_bound)
        self.arm_angle_info[1] = np.clip(self.arm_angle_info[1], *self.action_arm_bound)
        self.arm_angle_info[2] = np.clip(self.arm_angle_info[2], *self.action_arm_bound)


        # 如果手指接触到蓝色的 goal, 我们判定结束回合 (done)
        # 所以需要计算 finger 的坐标
        a1l = self.arm_info['l'][0]
        a2l = self.arm_info['l'][1]
        a3l = self.arm_info['l'][2]
        a4l = self.arm_info['l'][3]

        a1r = np.pi / 2
        (a2r, a3r, a4r) = self.arm_angle_info  # radian, angle

        a1xy = [0, 0]
        a2xy = [0, 0]
        a3xy = [0, 0]
        a4xy = [0, 0]
        a1xy[0] = self.base_loc + [15, 15]  # a1 start (x0, y0)
        a1xy[1] = np.array([np.cos(a1r), np.sin(a1r)]) * a1l + a1xy[0]  # a1 end and a2 start (x1, y1)
        a2xy[0] = a1xy[1]
        a2xy[1] = np.array([np.cos(a1r + a2r), np.sin(a1r + a2r)]) * a2l + a2xy[0]
        a3xy[0] = a2xy[1]
        a3xy[1] = np.array([np.cos(a1r + a2r + a3r), np.sin(a1r + a2r + a3r)]) * a3l + a3xy[0]
        a4xy[0] = a3xy[1]
        a4xy[1] = np.array([np.cos(a1r + a2r + a3r + a4r), np.sin(a1r + a2r + a3r + a4r)]) * a4l + a4xy[0]
        finger = a4xy[1]

        # 归一化，解决测试时超出运动范围而导致的泛化问题。
        # X_Train = 260.8, X_Test = 521.6
        # Y_Train = 74.5, y_Test = 149
        dist1 = [(self.goal['x'] - a1xy[1][0]), (self.goal['y'] - a1xy[1][1])]
        if abs(dist1[0]) <= ARM_X_DOMAIN:
            dist1[0] = dist1[0] / ARM_X_DOMAIN
        else:
            dist1[0] = ((abs(dist1[0]) - ARM_X_DOMAIN) / (X_DOMAIN - ARM_X_DOMAIN) + 1) * (dist1[0] / abs(dist1[0]))

        if abs(dist1[1]) <= ARM_Y_DOMAIN:
            dist1[1] = dist1[1] / ARM_Y_DOMAIN
        else:
            dist1[1] = ((abs(dist1[1]) - ARM_Y_DOMAIN) / (Y_DOMAIN - ARM_Y_DOMAIN) + 1) * (dist1[1] / abs(dist1[1]))

        dist1_ = np.sqrt(dist1[0] ** 2 + dist1[1] ** 2)
        dist2 = [(self.goal['x'] - a2xy[1][0]), (self.goal['y'] - a2xy[1][1])]
        if abs(dist2[0]) <= ARM_X_DOMAIN:
            dist2[0] = dist2[0] / ARM_X_DOMAIN
        else:
            dist2[0] = ((abs(dist2[0]) - ARM_X_DOMAIN) / (X_DOMAIN - ARM_X_DOMAIN) + 1) * (dist2[0] / abs(dist2[0]))

        if abs(dist2[1]) <= ARM_Y_DOMAIN:
            dist2[1] = dist2[1] / ARM_Y_DOMAIN
        else:
            dist2[1] = ((abs(dist2[1]) - ARM_Y_DOMAIN) / (Y_DOMAIN - ARM_Y_DOMAIN) + 1) * (dist2[1] / abs(dist2[1]))

        dist3 = [(self.goal['x'] - a3xy[1][0]), (self.goal['y'] - a3xy[1][1])]
        if abs(dist3[0]) <= ARM_X_DOMAIN:
            dist3[0] = dist3[0] / ARM_X_DOMAIN
        else:
            dist3[0] = ((abs(dist3[0]) - ARM_X_DOMAIN) / (X_DOMAIN - ARM_X_DOMAIN) + 1) * (dist3[0] / abs(dist3[0]))

        if abs(dist3[1]) <= ARM_Y_DOMAIN:
            dist3[1] = dist3[1] / ARM_Y_DOMAIN
        else:
            dist3[1] = ((abs(dist3[1]) - ARM_Y_DOMAIN) / (Y_DOMAIN - ARM_Y_DOMAIN) + 1) * (dist3[1] / abs(dist3[1]))

        dist3_ = np.sqrt(dist3[0] ** 2 + dist3[1] ** 2)
        dist4 = [(self.goal['x'] - finger[0]), (self.goal['y'] - finger[1])]
        if abs(dist4[0]) <= ARM_X_DOMAIN:
            dist4[0] = dist4[0] / ARM_X_DOMAIN
        else:
            dist4[0] = ((abs(dist4[0]) - ARM_X_DOMAIN) / (X_DOMAIN - ARM_X_DOMAIN) + 1) * (dist4[0] / abs(dist4[0]))

        if abs(dist4[1]) <= ARM_Y_DOMAIN:
            dist4[1] = dist4[1] / ARM_Y_DOMAIN
        else:
            dist4[1] = ((abs(dist4[1]) - ARM_Y_DOMAIN) / (Y_DOMAIN - ARM_Y_DOMAIN) + 1) * (dist4[1] / abs(dist4[1]))

        dist = np.sqrt(dist4[0] ** 2 + dist4[1] ** 2)

        # Reward
        r = (self.dist_ - dist) * 100
        r += r_angle
        r -= 1 / MAX_EP_STEPS * 100

        # if dist > self.dist_:
        #     r -= (dist - self.dist_) * 5
        self.dist_ = dist

        if dist3_ >= dist:
            r += 0.04
        if dist1_ < self.radius:
            r += 0.04
        # 根据 finger 和 goal 的坐标得出 done and reward
        if self.goal['x'] - self.goal['l'] / 2 < finger[0] < self.goal['x'] + self.goal['l'] / 2:
            if self.goal['y'] - self.goal['l'] / 2 < finger[1] < self.goal['y'] + self.goal['l'] / 2:

                # r = (self.dist_ - dist) * 10
                self.on_goal += 1
                if self.on_goal > 100:
                    done = True
                    r += 100 * 1 / dist

                    if self.goal['x'] - self.goal['l'] / 10 < finger[0] < self.goal['x'] + self.goal['l'] / 10:
                        if self.goal['y'] - self.goal['l'] / 10 < finger[1] < self.goal['y'] + self.goal['l'] / 10:
                            r += 1000
        else:
            self.on_goal = 0

        if np.sum(np.absolute(action)) <= 0.0001:
            self.STU_FLAG += 1
            if self.STU_FLAG >= 101:
                r -= 1 * self.STU_FLAG
        else:
            self.STU_FLAG = 0


        # state
        self.s = np.concatenate(([a2r, a3r, a4r, dist1[0]], dist3, dist4, [1. if self.on_goal else 0.]))
        # [a2r, a3r, a4r],
        return self.s, r, done, info

    def reset(self):

        # self.goal['x'] = np.random.rand() * 400.
        self.goal['y'] = np.random.rand() * 149. + 193.
        #########################################

        # ran = np.random.rand()
        # if ran <=0.20:
        #     self.goal['y'] = 193.
        # elif ran > 0.20 and ran <= 0.40:
        #     self.goal['y'] = 193. + 149./5
        # elif ran > 0.40 and ran <= 0.60:
        #     self.goal['y'] = 193. + 149. * 2 / 5
        # elif ran > 0.60 and ran <= 0.80:
        #     self.goal['y'] = 193. + 149. * 3 / 5
        # elif ran > 0.80 and ran <= 0.95:
        #     self.goal['y'] = 193. + 149. * 4 / 5
        # else:
        #     self.goal['y'] = 193. + 149.

        # if self.t <= ALPHA:
        #     self.goal['y'] = np.random.rand() * 149. + 193.
        # else:
        #####################################################
        # ran = np.random.rand()
        # if ran <= 0.33:
        #     self.goal['y'] = 193.
        # elif ran > 0.33 and ran <= 0.66:
        #     self.goal['y'] = 193. + 149. / 2
        # else:
        #     self.goal['y'] = 193. + 149.
        #####################################################

        # if self.t <= ALPHA + BELTA * 2 / 3:
        #     if self.t <= ALPHA + BELTA / 3:
        #             if self.t <= ALPHA:
        #                 self.goal['y'] = np.random.rand() * 149. + 193.
        #                 # ran = np.random.rand()
        #                 # if ran <= 0.375:
        #                 #     self.goal['y'] = 193.
        #                 # elif ran > 0.375 and ran <= 0.625:
        #                 #     self.goal['y'] = 193. + 149. / 2
        #                 # else:
        #                 #     self.goal['y'] = 193. + 149.
        #             else:
        #                 self.goal['y'] = 193. + 149. / 2
        #                 print(self.t)
        #     else:
        #         # 193+149/2 ~ 193+149
        #         self.goal['y'] = 193. + 149.  # * ((self.t - ALPHA - BELTA / 3) / BELTA * 3 / 2 + 0.5)
        # else:
        #     # 193+149/2 ~ 193
        #     self.goal['y'] = 193.  # + 149. * ((ALPHA + BELTA * 2 / 3 - self.t) / BELTA * 3 / 2 + 0.5)
        #
        self.t += 1

        self.arm_angle_info = (np.random.rand(3) - 0.5) * 2 * np.pi/2
        self.base_loc[0] = (np.random.rand(1) - 0.5) * 2 * 170 + 200

        self.on_goal = 0
        a1l = self.arm_info['l'][0]
        a2l = self.arm_info['l'][1]
        a3l = self.arm_info['l'][2]
        a4l = self.arm_info['l'][3]

        a1r = np.pi / 2
        (a2r, a3r, a4r) = self.arm_angle_info  # radian, angle

        a1xy = [0, 0]
        a2xy = [0, 0]
        a3xy = [0, 0]
        a4xy = [0, 0]

        a1xy[0] = self.base_loc + [15, 15]  # a1 start (x0, y0)
        a1xy[1] = np.array([np.cos(a1r), np.sin(a1r)]) * a1l + a1xy[0]  # a1 end and a2 start (x1, y1)
        a2xy[0] = a1xy[1]
        a2xy[1] = np.array([np.cos(a1r + a2r), np.sin(a1r + a2r)]) * a2l + a2xy[0]
        a3xy[0] = a2xy[1]
        a3xy[1] = np.array([np.cos(a1r + a2r + a3r), np.sin(a1r + a2r + a3r)]) * a3l + a3xy[0]
        a4xy[0] = a3xy[1]
        a4xy[1] = np.array([np.cos(a1r + a2r + a3r + a4r), np.sin(a1r + a2r + a3r + a4r)]) * a4l + a4xy[0]
        finger = a4xy[1]
        # normalize features
        dist1 = [(self.goal['x'] - a1xy[1][0]), (self.goal['y'] - a1xy[1][1])]
        if abs(dist1[0]) <= ARM_X_DOMAIN:
            dist1[0] = dist1[0] / ARM_X_DOMAIN
        else:
            dist1[0] = ((abs(dist1[0]) - ARM_X_DOMAIN) / (X_DOMAIN - ARM_X_DOMAIN) + 1) * (dist1[0] / abs(dist1[0]))

        if abs(dist1[1]) <= ARM_Y_DOMAIN:
            dist1[1] = dist1[1] / ARM_Y_DOMAIN
        else:
            dist1[1] = ((abs(dist1[1]) - ARM_Y_DOMAIN) / (Y_DOMAIN - ARM_Y_DOMAIN) + 1) * (dist1[1] / abs(dist1[1]))

        # dist1_ = np.sqrt(dist1[0] ** 2 + dist1[1] ** 2)
        dist2 = [(self.goal['x'] - a2xy[1][0]), (self.goal['y'] - a2xy[1][1])]
        if abs(dist2[0]) <= ARM_X_DOMAIN:
            dist2[0] = dist2[0] / ARM_X_DOMAIN
        else:
            dist2[0] = ((abs(dist2[0]) - ARM_X_DOMAIN) / (X_DOMAIN - ARM_X_DOMAIN) + 1) * (dist2[0] / abs(dist2[0]))

        if abs(dist2[1]) <= ARM_Y_DOMAIN:
            dist2[1] = dist2[1] / ARM_Y_DOMAIN
        else:
            dist2[1] = ((abs(dist2[1]) - ARM_Y_DOMAIN) / (Y_DOMAIN - ARM_Y_DOMAIN) + 1) * (dist2[1] / abs(dist2[1]))

        dist3 = [(self.goal['x'] - a3xy[1][0]), (self.goal['y'] - a3xy[1][1])]
        if abs(dist3[0]) <= ARM_X_DOMAIN:
            dist3[0] = dist3[0] / ARM_X_DOMAIN
        else:
            dist3[0] = ((abs(dist3[0]) - ARM_X_DOMAIN) / (X_DOMAIN - ARM_X_DOMAIN) + 1) * (dist3[0] / abs(dist3[0]))

        if abs(dist3[1]) <= ARM_Y_DOMAIN:
            dist3[1] = dist3[1] / ARM_Y_DOMAIN
        else:
            dist3[1] = ((abs(dist3[1]) - ARM_Y_DOMAIN) / (Y_DOMAIN - ARM_Y_DOMAIN) + 1) * (dist3[1] / abs(dist3[1]))

        # dist3_ = np.sqrt(dist3[0] ** 2 + dist3[1] ** 2)
        dist4 = [(self.goal['x'] - finger[0]), (self.goal['y'] - finger[1])]
        if abs(dist4[0]) <= ARM_X_DOMAIN:
            dist4[0] = dist4[0] / ARM_X_DOMAIN
        else:
            dist4[0] = ((abs(dist4[0]) - ARM_X_DOMAIN) / (X_DOMAIN - ARM_X_DOMAIN) + 1) * (dist4[0] / abs(dist4[0]))

        if abs(dist4[1]) <= ARM_Y_DOMAIN:
            dist4[1] = dist4[1] / ARM_Y_DOMAIN
        else:
            dist4[1] = ((abs(dist4[1]) - ARM_Y_DOMAIN) / (Y_DOMAIN - ARM_Y_DOMAIN) + 1) * (dist4[1] / abs(dist4[1]))

        dist = np.sqrt(dist4[0] ** 2 + dist4[1] ** 2)
        self.dist_ = dist
        # state
        self.s = np.concatenate(([a2r, a3r, a4r, dist1[0]], dist3, dist4, [1. if self.on_goal else 0.]))
        # [a2r, a3r, a4r]

        return self.s
    def get_state(self):
        return self.s
    def render(self):
        if self.viewer is None:  # 如果调用了 render, 而且没有 viewer, 就生成一个
            self.viewer = Viewer(self.arm_info, self.arm_angle_info, self.goal, self.base_loc)
        self.viewer.render(self.arm_info, self.arm_angle_info, self.base_loc)  # 使用 Viewer 中的 render 功能

    def sample_action(self):
        return (np.random.rand(3) - 0.5)*4, (np.random.rand(1) - 0.5)*50
        # return np.array([0.5, 0.5, 0.5, 0.5]) - 0.5, np.array([0.5]) - 0.5


class Viewer(pyglet.window.Window):
    bar_thc = 5

    def __init__(self, arm_info, arm_angle_info, goal, base_loc):  # 画出手臂等
        # 创建窗口的继承
        # vsync 如果是 True, 按屏幕频率刷新, 反之不按那个频率
        super(Viewer, self).__init__(width=400, height=400, resizable=False, caption='Arm', vsync=False)

        # 窗口背景颜色
        pyglet.gl.glClearColor(1, 1, 1, 1)

        # 添加 arm 信息
        self.arm_info = arm_info
        self.arm_angle_info = arm_angle_info
        self.goal_info = goal

        # 添加窗口中心点, 手臂的根
        self.center_coord = np.array([200, 200])
        self.base_loc = base_loc
        # 将手臂的作图信息放入这个 batch
        self.batch = pyglet.graphics.Batch()  # display whole batch at once

        # 蓝色 goal 的信息包括他的 x, y 坐标, goal 的长度 l
        self.goal = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,  # 4 corners
            ('v2f', [goal['x'] - goal['l'] / 2, goal['y'] - goal['l'] / 2,
                     goal['x'] - goal['l'] / 2, goal['y'] + goal['l'] / 2,
                     goal['x'] + goal['l'] / 2, goal['y'] + goal['l'] / 2,
                     goal['x'] + goal['l'] / 2, goal['y'] - goal['l'] / 2]),
            ('c3B', (86, 109, 249) * 4))  # color

        self.base = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,  # 4 corners
            ('v2f', [170, 185,
                     170, 215,
                     230, 185,
                     230, 215]),
            ('c3B', (86, 86, 86) * 4))  # color

        # 添加手臂
        self.arm1 = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,
            ('v2f', [250, 250,  # 同上, 点信息
                     250, 286.2,
                     260, 286.2,
                     260, 250]),
            ('c3B', (249, 86, 86) * 4,))  # color

        self.arm2 = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,
            ('v2f', [270, 250,  # 同上, 点信息
                     270, 282.5,
                     280, 282.5,
                     280, 250]),
            ('c3B', (249, 86, 86) * 4,))  # color
        self.arm3 = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,
            ('v2f', [290, 250,  # 同上, 点信息
                     290, 282.5,
                     300, 282.5,
                     300, 250]),
            ('c3B', (249, 86, 86) * 4,)) # color
        self.arm4 = self.batch.add(
            4, pyglet.gl.GL_QUADS, None,
            ('v2f', [310, 250,  # 同上, 点信息
                     310, 275.6,
                     320, 275.6,
                     320, 250]),
            ('c3B', (249, 86, 86) * 4,))  # color

    def render(self, arm_info, arm_angle_info, base_loc):  # 刷新并呈现在屏幕上
        self._update_arm(arm_info, arm_angle_info, base_loc)  # 更新手臂内容 (暂时没有变化)
        self.switch_to()
        self.dispatch_events()
        self.dispatch_event('on_draw')
        self.flip()

    def on_draw(self):  # 刷新手臂等位置
        self.clear()  # 清屏
        self.batch.draw()  # 画上 batch 里面的内容

    def _update_arm(self, arm_info, arm_angle_info, base_loc): # 更新手臂的位置信息

        self.goal.vertices = (
            self.goal_info['x'] - self.goal_info['l']/2, self.goal_info['y'] - self.goal_info['l']/2,
            self.goal_info['x'] + self.goal_info['l']/2, self.goal_info['y'] - self.goal_info['l']/2,
            self.goal_info['x'] + self.goal_info['l']/2, self.goal_info['y'] + self.goal_info['l']/2,
            self.goal_info['x'] - self.goal_info['l']/2, self.goal_info['y'] + self.goal_info['l']/2)

        a1l = arm_info['l'][0]
        a2l = arm_info['l'][1]
        a3l = arm_info['l'][2]
        a4l = arm_info['l'][3]

        a1r = np.pi / 2
        a2r = arm_angle_info[0]  # radian, angle
        a3r = arm_angle_info[1]
        a4r = arm_angle_info[2]

        a1xy = [0, 0]
        a2xy = [0, 0]
        a3xy = [0, 0]
        a4xy = [0, 0]

        a1xy[0] = base_loc + np.array([15, 15])  # a1 start (x0, y0)
        a1xy[1] = np.array([np.cos(a1r), np.sin(a1r)]) * a1l + a1xy[0]  # a1 end and a2 start (x1, y1)
        a2xy[0] = a1xy[1]
        a2xy[1] = np.array([np.cos(a1r + a2r), np.sin(a1r + a2r)]) * a2l + a2xy[0]
        a3xy[0] = a2xy[1]
        a3xy[1] = np.array([np.cos(a1r + a2r + a3r), np.sin(a1r + a2r + a3r)]) * a3l + a3xy[0]
        a4xy[0] = a3xy[1]
        a4xy[1] = np.array([np.cos(a1r + a2r + a3r + a4r), np.sin(a1r + a2r + a3r + a4r)]) * a4l + a4xy[0]

        xy01 = base_loc + [-30, -15]
        xy02 = base_loc + [-30,  15]
        xy03 = base_loc + [ 30,  15]
        xy04 = base_loc + [ 30, -15]

        # 第一段手臂的4个点信息
        a1tr = 0  # np.pi / 2
        a2tr = arm_angle_info[0]
        a3tr = arm_angle_info[0] + arm_angle_info[1]
        a4tr = arm_angle_info[0] + arm_angle_info[1] + arm_angle_info[2]
        xy11 = a1xy[0] + np.array([ np.cos(a1tr),  np.sin(a1tr)]) * self.bar_thc
        xy12 = a1xy[0] + np.array([-np.cos(a1tr), -np.sin(a1tr)]) * self.bar_thc
        xy13 = a1xy[1] + np.array([-np.cos(a1tr), -np.sin(a1tr)]) * self.bar_thc
        xy14 = a1xy[1] + np.array([ np.cos(a1tr),  np.sin(a1tr)]) * self.bar_thc

        # 第二段手臂的4个点信息
        xy21 = a2xy[0] + np.array([ np.cos(a2tr),  np.sin(a2tr)]) * self.bar_thc
        xy22 = a2xy[0] + np.array([-np.cos(a2tr), -np.sin(a2tr)]) * self.bar_thc
        xy23 = a2xy[1] + np.array([-np.cos(a2tr), -np.sin(a2tr)]) * self.bar_thc
        xy24 = a2xy[1] + np.array([ np.cos(a2tr),  np.sin(a2tr)]) * self.bar_thc

        # 第3段手臂的4个点信息
        xy31 = a3xy[0] + np.array([ np.cos(a3tr),  np.sin(a3tr)]) * self.bar_thc
        xy32 = a3xy[0] + np.array([-np.cos(a3tr), -np.sin(a3tr)]) * self.bar_thc
        xy33 = a3xy[1] + np.array([-np.cos(a3tr), -np.sin(a3tr)]) * self.bar_thc
        xy34 = a3xy[1] + np.array([ np.cos(a3tr),  np.sin(a3tr)]) * self.bar_thc

        # 第4段手臂的4个点信息
        xy41 = a4xy[0] + np.array([ np.cos(a4tr),  np.sin(a4tr)]) * self.bar_thc
        xy42 = a4xy[0] + np.array([-np.cos(a4tr), -np.sin(a4tr)]) * self.bar_thc
        xy43 = a4xy[1] + np.array([-np.cos(a4tr), -np.sin(a4tr)]) * self.bar_thc
        xy44 = a4xy[1] + np.array([ np.cos(a4tr),  np.sin(a4tr)]) * self.bar_thc

        # 将点信息都放入手臂显示中
        self.base.vertices = np.concatenate((xy01, xy02, xy03, xy04))
        self.arm1.vertices = np.concatenate((xy11, xy12, xy13, xy14))
        self.arm2.vertices = np.concatenate((xy21, xy22, xy23, xy24))
        self.arm3.vertices = np.concatenate((xy31, xy32, xy33, xy34))
        self.arm4.vertices = np.concatenate((xy41, xy42, xy43, xy44))

    # def on_mouse_motion(self, x, y, dx, dy):
    #     self.goal_info['x'] = x
    #     self.goal_info['y'] = y


if __name__ == '__main__':
    env = mlRoboEnv()
    STEPS = 500
    while True:
        env.reset()
        # env.render()
        for i in range(STEPS):
            env.render()
            (action_arm, action_base) = env.sample_action()
            action = np.append(action_arm, action_base)
            env.step(action)
