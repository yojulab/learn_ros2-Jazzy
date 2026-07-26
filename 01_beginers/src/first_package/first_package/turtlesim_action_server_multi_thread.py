import math
import time

import rclpy
from geometry_msgs.msg import Twist
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
        super().__init__('dist_turtle_action_server')
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

        loop_period_seconds = 0.1
        estimated_distance = 0.0

        while estimated_distance < goal_handle.request.distance:
            estimated_distance += abs(velocity_message.linear.x) * loop_period_seconds
            feedback_message.remaining_distance = max(
                0.0,
                goal_handle.request.distance - estimated_distance,
            )
            goal_handle.publish_feedback(feedback_message)
            self.publisher.publish(velocity_message)
            time.sleep(loop_period_seconds)

        goal_handle.succeed()
        result = MoveDistance.Result()
        result.position_x = self.current_pose.x
        result.position_theta = self.current_pose.theta
        result.result_distance = estimated_distance
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
