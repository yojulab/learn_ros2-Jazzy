# Intermediates - ROS2 Learning

## Summary

This directory contains intermediate-level ROS2 learning materials and packages.

### Create package with node
```bash
02_Intermediates$ mkdir src
sanghun-oh@sanghun-oh-ROS2-Jazzy:~/ros-ws/learn_ros2-Jazzy/02_Intermediates$ cd src/
sanghun-oh@sanghun-oh-ROS2-Jazzy:~/ros-ws/learn_ros2-Jazzy/02_Intermediates/src$ ls
sanghun-oh@sanghun-oh-ROS2-Jazzy:~/ros-ws/learn_ros2-Jazzy/02_Intermediates/src$ ros2 p
param   pkg     plugin  
sanghun-oh@sanghun-oh-ROS2-Jazzy:~/ros-ws/learn_ros2-Jazzy/02_Intermediates/src$ ros2 pkg create --build-type ament_python --node-name first_node first_package
sanghun-oh@sanghun-oh-ROS2-Jazzy:~/ros-ws/learn_ros2-Jazzy/02_Intermediates/src$ cd ..
sanghun-oh@sanghun-oh-ROS2-Jazzy:~/ros-ws/learn_ros2-Jazzy/02_Intermediates$ col
col       colcon    colcrt    colormgr  colrm     column    
sanghun-oh@sanghun-oh-ROS2-Jazzy:~/ros-ws/learn_ros2-Jazzy/02_Intermediates$ colcon build
Starting >>> first_package
Finished <<< first_package [1.09s]          

Summary: 1 package finished [1.24s]
sanghun-oh@sanghun-oh-ROS2-Jazzy:~/ros-ws/learn_ros2-Jazzy/02_Intermediates$ ros2 run first_package first_node
Package 'first_package' not found
sanghun-oh@sanghun-oh-ROS2-Jazzy:~/ros-ws/learn_ros2-Jazzy/02_Intermediates$ ls
build  install  log  README.md  src
sanghun-oh@sanghun-oh-ROS2-Jazzy:~/ros-ws/learn_ros2-Jazzy/02_Intermediates$ source ./install/local_setup.bash 
sanghun-oh@sanghun-oh-ROS2-Jazzy:~/ros-ws/learn_ros2-Jazzy/02_Intermediates$ ros2 run first_package first_node
Hi from first_package.
```
### Running the First Node

To run the `first_node` from the `first_package`, use the following command:

```bash
ros2 run first_package first_node
```

**Status**: ✓ Successfully executed (Exit Code: 0)

### Project Structure

- `src/first_package/` - Main ROS2 package containing the first_node implementation
