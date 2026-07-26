from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [
            Node (
                namespace= "turtlesim", package='turtlesim', 
                executable='turtlesim_node', output='screen'),
            Node (
                namespace= "first_cmd_vel", package='first_package', 
                executable='turtlesim_publisher', output='screen'),            
        ]
    )