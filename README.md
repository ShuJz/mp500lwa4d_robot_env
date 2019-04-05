# mp500lwa4d_robot_env
There are ROS packages of a mobile robot, consists of mobile base([neo_mp_500](https://github.com/neobotix/neo_mp_500)), arm([lwa4d](https://github.com/ipa320/schunk_modular_robotics/tree/indigo_dev/schunk_description)) and gripper([PG-plus70](https://github.com/ShuJz/schunk_modular_robotics)), and a OpenAI.gym-based enviroment interface.

![3dRobot](https://github.com/ShuJz/mp500lwa4d_robot_env/blob/master/3dRobot.png)

![system](https://github.com/ShuJz/mp500lwa4d_robot_env/blob/master/system.png)

Before train the model, pleace determine the default version of Python you are using,

- if it is Python2: you should install gym package in Python2
- if it is Python3: you should install ROS in python3.6 enviroment. For how to install ROS kinetic in python3.6 enviroment, please see the document < Install ROS-Kinetic with Python3.md >



To train the model with a DDPG Agent:

1. Set param ON_TRAIN in script main_distri.py line 19 and RLAgent.py line 12
```python
ON_TRAIN = True
```
2. Then run in bash
````bash
conda activate mp500lwa4d_gym
roslaunch mp500lwa4d_description RL_gazebo_distri.launch
rosrun robot_service RLAgent.py
rosrun robot_service main_distri.py
````

