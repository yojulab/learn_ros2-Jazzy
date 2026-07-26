import rclpy as rp
from rclpy.executors import MultiThreadedExecutor

from .turtlesim_publisher import SimplePublisher
from .turtlesim_subscriber import TurtlesimSubscriber


def main(args=None):
    rp.init(args=args)
    sub = TurtlesimSubscriber()
    pub = SimplePublisher()
    executor = MultiThreadedExecutor()
    executor.add_node(sub)
    executor.add_node(pub)

    try:
        executor.spin()
    finally:
        executor.shutdown()
        sub.destroy_node()
        pub.destroy_node()
        rp.shutdown()


if __name__ == '__main__':
    main()
