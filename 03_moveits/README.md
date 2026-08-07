
## sample zip
- fromm https://www.youtube.com/watch?v=-xDyxxRiW7M&t=3361s
- from source : https://drive.google.com/file/d/1i2TBP4j3NeCgSHMOVPKoQGhO1LbuvvG8/view

## with riv2
```bash
ros2 launch my_robot_description display.launch.xml
ros2 launch my_robot_description display_with_collision.launch.xml
ros2 run tf2_tools view_frames
```
## 자동 충돌 설정
- target : ls src/my_robot_description/urdf/my_robot_with_collision.urdf.xacro
```bash
ros2 launch moveit_setup_assistant setup_assistant.launch.py
```
