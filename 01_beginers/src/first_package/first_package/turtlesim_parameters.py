import math
import time

import rclpy
from geometry_msgs.msg import Twist
from rcl_interfaces.msg import ParameterDescriptor, SetParametersResult, FloatingPointRange
from rclpy.action import ActionServer
from rclpy.executors import MultiThreadedExecutor
from rclpy.node import Node
from turtlesim.msg import Pose

from first_package.turtlesim_subscriber import TurtlesimSubscriber
from first_package_msgs.action import MoveDistance


class TurtlePoseSubscriber(TurtlesimSubscriber):
    def __init__(self, action_server_node):
        super().__init__()
        self.action_server_node = action_server_node

    def callback(self, msg):
        self.action_server_node.current_pose = msg


class DistTurtleActionServer(Node):
    def __init__(self):
        super().__init__('turtlesim_parameters')
        self.total_distance = 0.0
        self.is_first_pose = True
        self.current_pose = Pose()
        self.previous_pose = Pose()
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.action_server = ActionServer(
            self,
            MoveDistance,
            'dist_turtle',
            execute_callback=self.execute_callback,
        )

        param_desc_quantile = ParameterDescriptor(
            description='Quantile time parameter',
            floating_point_range=[FloatingPointRange(from_value=0.0, to_value=1.0, step=0.01)],
        )
        self.declare_parameter('quantile_time', 0.75, param_desc_quantile)
        param_desc_almost_goal = ParameterDescriptor(
            description='Almost goal time parameter',
            read_only=False,
            dynamic_typing=True
        )
        self.declare_parameter('almost_goal_time', 0.95, param_desc_almost_goal)
        quantile_time_parameter, almost_goal_time_parameter = self.get_parameters(
            ['quantile_time', 'almost_goal_time']
        )
        self.get_logger().info(
            f'quantile_time: {quantile_time_parameter.value}'
        )
        self.get_logger().info(
            f'almost_goal_time: {almost_goal_time_parameter.value}'
        )

        self.quantile_time = quantile_time_parameter.value
        self.almost_goal_time = almost_goal_time_parameter.value
        self.add_on_set_parameters_callback(self.parameter_callback)

    def parameter_callback(self, params):
        for parameter in params:
            self.get_logger().info(
                f'{parameter.name} is changed to {parameter.value}'
            )
            if parameter.name == 'quantile_time':
                self.quantile_time = parameter.value
            if parameter.name == 'almost_goal_time':
                self.almost_goal_time = parameter.value
        return SetParametersResult(successful=True)

    def calculate_distance(self):
        if self.is_first_pose:
            self.previous_pose.x = self.current_pose.x
            self.previous_pose.y = self.current_pose.y
            self.is_first_pose = False
            return 0.0

        distance = math.sqrt(
            (self.current_pose.x - self.previous_pose.x) ** 2
            + (self.current_pose.y - self.previous_pose.y) ** 2
        )
        self.previous_pose = self.current_pose
        return distance

    def execute_callback(self, goal_handle):
        feedback_message = MoveDistance.Feedback()
        velocity_message = Twist()
        velocity_message.linear.x = goal_handle.request.linear_x
        velocity_message.angular.z = goal_handle.request.angular_z

        while self.total_distance < goal_handle.request.distance:
            self.total_distance += self.calculate_distance()
            feedback_message.remaining_distance = max(
                0.0,
                goal_handle.request.distance - self.total_distance,
            )
            goal_handle.publish_feedback(feedback_message)
            self.publisher.publish(velocity_message)
            time.sleep(0.01)

        goal_handle.succeed()
        result = MoveDistance.Result()
        result.position_x = self.current_pose.x
        result.position_theta = self.current_pose.theta
        result.result_distance = self.total_distance
        self.total_distance = 0.0
        self.is_first_pose = True
        return result


def main(args=None):
    rclpy.init(args=args)
    executor = MultiThreadedExecutor()
    action_server = DistTurtleActionServer()
    pose_subscriber = TurtlePoseSubscriber(action_server)
    executor.add_node(pose_subscriber)
    executor.add_node(action_server)

    try:
        executor.spin()
    finally:
        executor.shutdown()
        pose_subscriber.destroy_node()
        action_server.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
