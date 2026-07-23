import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class SimplePublisher(Node):
    def __init__(self):
        super().__init__('simple_publisher')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer_ = self.create_timer(0.1, self.publish_velocity)

    def publish_velocity(self):
        msg = Twist()
        msg.linear.x = 3.0
        msg.angular.z = 2.0
        self.publisher_.publish(msg)
        self.get_logger().info(
            'Published: linear.x=%.2f, angular.z=%.2f' % (msg.linear.x, msg.angular.z)
        )


def main():
    rclpy.init()
    simple_publisher = SimplePublisher()
    rclpy.spin(simple_publisher)
    simple_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()