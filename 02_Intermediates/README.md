## from github
```bash
wget https://raw.githubusercontent.com/PinkWink/for_ROS2_study/refs/heads/main/R2R%20%EC%8B%AC%ED%99%94%ED%8E%B8%20gazebo%20tutorials/building_robot.sdf
gz sim building_robot.sdf
```
```bash
https://github.com/PinkWink/pinky_for_edu
$ source install/setup.bash 
ros2 launch pinky_description display.launch.xml
ros2 run tf2_tools view_frames
ros2 launch pinky_description display.launch.xml
ros2 launch pinky_description rviz2_test.launch.xml

```
## simulation
```bash
ros2 launch pinky_gazebo launch_sim_empty.launch.xml
ros2 launch pinky_gazebo launch_sim.launch.xml
```

## slam
```bash
rosdep update
ros2 launch pinky_gazebo launch_sim.launch.xml
ros2 launch pinky navigation map_building.launch.xml use_sim_time:=true
ros2 launch pinky_navigation map_view.launch.xml
ros2 run teleop_twist_keyboard teleop_twist_keyboard
ros2 run nav2_map_server map_saver_cli-f<저장할 맵이름>
``` 