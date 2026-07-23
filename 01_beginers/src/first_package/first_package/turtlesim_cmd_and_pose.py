import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from first_package_msgs.msg import CmdAndPoseVel


class TurtlesimCmdAndPose(Node):
    def __init__(self):
        super().__init__('turtlesim_cmd_and_pose')
        self.subscription_pose = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.callback_pose,
            10
        )
        self.subscription_twist = self.create_subscription(
            Twist,
            '/turtle1/cmd_vel',
            self.callback_twist,
            10
        )
        self.cmd_and_pose = CmdAndPoseVel()

    def callback_pose(self, msg):
        self.cmd_and_pose.pose_x = msg.x
        self.cmd_and_pose.pose_y = msg.y
        self.cmd_and_pose.linear_vel = msg.linear_velocity
        self.cmd_and_pose.angular_vel = msg.angular_velocity
        print(self.cmd_and_pose)

    def callback_twist(self, msg):
        self.cmd_and_pose.cmd_vel_linear = msg.linear.x
        self.cmd_and_pose.cmd_vel_angular = msg.angular.z
        print(self.cmd_and_pose)


def main():
    rclpy.init()
    turtlesim_cmd_and_pose_node = TurtlesimCmdAndPose()
    rclpy.spin(turtlesim_cmd_and_pose_node)
    turtlesim_cmd_and_pose_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()