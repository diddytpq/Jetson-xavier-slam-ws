# Jetson-xavier-slam-ws
Jetson xavier slam workspace

## 1. Dependency

### 1.1. pcl ver --> 1.10  
	https://ropiens.tistory.com/65
### 1.2 GTSAM
	https://github.com/borglab/gtsam/tree/4.0.2


## 2. check usb port and port permission 
	ls /dev/ttyUSB* 
	sudo chmod 666 /dev/tty*

## 3. Record topic
	rosbag record /velodyne_points /tf /imu/data
	roscore
	rosparam set /use_sim_time true
	rosbag play --clock --pause rosbag/*.bag

## 4. Run lio sam 
	roslaunch velodyne_pointcloud VLP16_points.launch
	roslaunch ros-ngimu run.launch

	roslaunch lio_sam run.launch 
	rosbag play --clock --pause rosbag/*.bag --topic /velodyne_points /tf /imu/data

## 5. Run mecanum_robot_control_joy
	roslaunch openrobot_control openrobot_control_6omni.launch


## 6. trouble shooting
* cv_bridge Error
	```
	https://jstar0525.tistory.com/118
	```
