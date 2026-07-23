# Intermediates - ROS2 Learning

## Summary

This directory contains intermediate-level ROS2 learning materials and packages.

### Create package with node

```bash
mkdir src
cd src/
ros2 pkg create --build-type ament_python --node-name first_node first_package
cd ..
colcon build
source ./install/local_setup.bash 
ros2 run first_package first_node
```

**Status**: ✓ Successfully executed

### Create Custom Message Package

```bash
ros2 pkg create --build-type ament_cmake first_package_msgs
cd src/first_package_msgs
mkdir msg
```

Create `CmdAndPoseVel.msg` with the following content:
```
float32 cmd_vel_linear
float32 cmd_vel_angular

float32 pose_x
float32 pose_y
float32 linear_vel
float32 angular_vel
```

### Build and Verify Custom Message

```bash
colcon build
source install/setup.bash
ros2 interface show first_package_msgs/msg/CmdAndPoseVel
ros2 interface list | grep CmdAndPoseVel
```

**Output**:
```
first_package_msgs/msg/CmdAndPoseVel
```

**Status**: ✓ Successfully registered and available

### Project Structure

- `src/first_package/` - Main ROS2 package containing the first_node implementation
- `src/first_package_msgs/` - Custom message package with CmdAndPoseVel message definition

