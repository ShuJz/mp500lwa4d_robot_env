# mp500lwa4d_robot_env
There are ROS packages of a mobile robot, compose of mobile base([neo_mp_500](https://github.com/neobotix/neo_mp_500)) and arm([lwa4d](https://github.com/ipa320/schunk_modular_robotics/tree/indigo_dev/schunk_description)), and a OpenAI.gym-based enviroment.

To train the model with a DDPG Agent:

````bash
conda activate mp500lwa4d_gym
roslaunch mp500lwa4d_description RL_gazebo_distri.launch
rosrun robot_service RLAgent.py
rosrun robot_service main_distri_modi.py
````

- mp500lwa4d_gym env. is based on python 3.6

For how to install ROS kinetic in python3.6 enviroment, please see the document < Install ROS-Kinetic with Python3.md >