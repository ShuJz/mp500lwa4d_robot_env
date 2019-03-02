# Install ROS-Kinetic, gym and baselines with Python3

## create virtual conda env

```bash
conda create -n mp500lwa4d_gym python=3.6
```

here onwards the installation continues in the conda environment created.

## ROS installation

``` bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
sudo apt-get update
sudo apt-get install ros-kinetic-desktop
sudo rosdep init
rosdep update
echo "source /opt/ros/kinetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt remove '.*gazebo.*' '.*sdformat.*' '.*ignition-.*'
```

## GAZEBO8 installation

```bash
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get install gazebo8
```

**reboot might be required if gazebo not launching:**

````bash
sudo apt-get install ros-kinetic-gazebo8-ros-pkgs ros-kinetic-gazebo8-ros-control
````

## rename cv2.so

**rename cv2.so to another name(cv2-renamed.so) at /opt/ros/kinetic/lib/python2.7/dist-packages/**

```bash
pip install opencv-python
pip install gym
```

## solving boost package error

**For solving the boost package error related to c make refer this [post](https://github.com/BVLC/caffe/issues/4843)**

```bash
cd /usr/lib/x86_64-linux-gnu
sudo ln -s libboost_python-py35.so libboost_python3.so 

pip install rospkg catkin_pkg

sudo apt-get install python3-pyqt4

sudo apt-get install \
cmake gcc g++ qt4-qmake libqt4-dev \
libusb-dev libftdi-dev \
python3-defusedxml python3-vcstool \
ros-kinetic-octomap-msgs        \
ros-kinetic-joy                 \
ros-kinetic-geodesy             \
ros-kinetic-octomap-ros         \
ros-kinetic-control-toolbox     \
ros-kinetic-pluginlib	       \
ros-kinetic-trajectory-msgs     \
ros-kinetic-control-msgs	       \
ros-kinetic-std-srvs 	       \
ros-kinetic-nodelet	       \
ros-kinetic-urdf		       \
ros-kinetic-rviz		       \
ros-kinetic-kdl-conversions     \
ros-kinetic-eigen-conversions   \
ros-kinetic-tf2-sensor-msgs     \
ros-kinetic-pcl-ros \
ros-kinetic-navigation

sudo apt-get install ros-kinetic-ar-track-alvar-msgs
sudo apt-get install ros-kinetic-sophus
sudo apt-get install git
```

## CATKIN IGNORE the 3 mentioned packages

- spacenav_node not compiling. CATKIN_IGNOREd.
- wiimote not compiling. CATKIN_IGNOREd.
- kobuki_qtestsuite not compiling. CATKIN_IGNOREd.

## Install gym-gazebo

```bash
git clone https://github.com/erlerobot/gym-gazebo
cd gym-gazebo
sudo pip3 install -e .

# Dependencies and libraries
sudo pip3 install h5py
sudo apt-get install python3-skimage

# install Theano
cd ~/
git clone git://github.com/Theano/Theano.git
cd Theano/
sudo python3 setup.py develop

#install Keras
sudo pip3 install keras
```

**Add 3 more packages to the file gazebo.repos locates in ~/gym-gazebo/gym_gazebo/envs . thes packages were related to open cv for ros**

```
geometry:
   type: git
   url: https://github.com/ros/geometry
   version: indigo-devel
 geometry2:
   type: git
   url: https://github.com/ros/geometry2
   version: indigo-devel
 vision_opencv:
   type: git
   url: https://github.com/ros-perception/vision_opencv.git
   version: kinetic
```

```bash
cd gym_gazebo/envs/installation
bash setup_kinetic.bash	
bash turtlebot_setup.bash
```

## Installation baselines

careful before installing Xorg that may distroy the X windows system.

会造成电脑卡在开机输入密码的画面，解决方法：

先将系统设置为开机直接进入命令行界面：

If you can't get in the desktop after installing Xorg, please try this:

go into system setting from GRUB:

```bash
sudo systemctl set-default multi-user.target
# 若要恢复图像界面启动
sudo systemctl set-default graphical.target
```



restall X windows:

```bash
# uninstall X windows
sudo apt-get purge xserver*
# install X windows
sudo apt-get update
sudo apt-get dist-upgrade

sudo apt-get install xserver-xorg
sudo apt-get install x-window-system-core
sudo apt-get install ubuntu-desktop

# start desktop
sudo service lightdm start
```

## Test

``` bash
conda activate mp500lwa4d_gym
roslaunch mp500lwa4d_description lwa4dmp500_sim.launch
```

1. Error：

```bash
ModuleNotFoundError: No module named 'defusedxml'
```

Solution：

```bash
pip install defusedxml
```

run again：

2. gazebo don't display the model，and throw out Error：

```bash
ImportError: dynamic module does not define module export function (PyInit__tf2)
```

Solution：

Building a new workspace ~/catkin_ws, and download resource of ros packages geometry and geometry2 in it, then catkin_make again, and source setup.bash.

在 catkin_ws/src 中下载 geometry 和 geometry2 的源代码，并在虚拟环境中重新编译。不能在 mp500lwa4d_env/src 中编译，因为这时使用的仍是Python2.7 编译，原因未知。

编译完成后需要重新 source catkin_ws

```bash
conda activate mp500lwa4d_gym
cd ~/catkin_ws/src
git clone https://github.com/ros/geometry %下载geometry和geometry2的源代码 
git clone https://github.com/ros/geometry2 
cd ../
catkin_make
```

3. Error：

   ```bash
   Could not load controller 'arm/joint_trajectory_controller' because controller type 'position_controllers/JointTrajectoryController' does not exist.
   ```

   Solution：

   ```bash
   sudo apt-get install ros-kinetic-position-controllers
   sudo apt-get install ros-kinetic-effort-controllers
   sudo apt-get install ros-kinetic-joint-state-controller
   sudo apt-get install ros-kinetic-joint-trajectory-controller
   ```

4. Error：

   ```bash
   ImportError for 'pyqt': No module named 'PyQt5'
   ImportError for 'pyside': No module named 'PySide2'
   ```

   Solution：

   ```bash
   pip install pyqt5
   pip install PySide2
   ```

5. Error：

   ``` python
   import moveit_commender
   ImportError: dynamic module does not define module export function (PyInit__moveit_roscpp_initializer)
   ```

   

   Solution：

   don't use moveit!

6. Python Error

   ```python
   from: can't read /var/mail/Bio
   ```

   Solution：

   add the following line to the top of the script:

   ```python
   #!/usr/bin/python
   ```

   

7. 



