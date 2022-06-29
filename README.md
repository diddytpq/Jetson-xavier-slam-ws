# Jetson-xavier-slam-ws
Jetson xavier slam workspace

##Dependency

pcl 1.8 > 
GTSAM
sudo add-apt-repository ppa:borglab/gtsam-release-4.0
sudo apt install libgtsam-dev libgtsam-unstable-dev

## check usb port and port permission 
```bash
ls /dev/ttyUSB* 
sudo chmod 666 /dev/tty*
```

## Record topic
```bash
rosbag record /velodyne_points /tf /imu/data
roscore
rosparam set /use_sim_time true
rosbag play --clock --pause rosbag/*.bag
```

## Run lio sam 
```bash
roslaunch velodyne_pointcloud VLP16_points.launch
roslaunch ros-ngimu run.launch

roslaunch lio-sam run.launch 
rosbag play --clock --pause rosbag/*.bag --topic /velodyne_points /tf /imu/data

```

## Run mecanum_robot_control_joy
```bash
roslaunch openrobot_control openrobot_control_6omni.launch
```

### trouble shooting

#### cv_bridge Error

##### https://jstar0525.tistory.com/118

