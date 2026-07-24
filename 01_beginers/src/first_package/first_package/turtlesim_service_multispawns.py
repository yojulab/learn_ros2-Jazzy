import math
import time

import rclpy
from rclpy.node import Node

from first_package_msgs.srv import MultiSpawn
from turtlesim.srv import Spawn


class MultiSpawning(Node):
    """ROS 2 node providing a service to spawn multiple turtles in turtlesim."""

    def __init__(self):
        super().__init__('multi_spawner')

        # Create the MultiSpawn service using the custom service type.
        self.srv = self.create_service(
            MultiSpawn,
            'multi_spawn',
            self.callback_service,
        )
        self.get_logger().info('MultiSpawn service ready.')

        # Create a client for the turtlesim spawn service.
        # This service is provided by the turtlesim node at /spawn.
        self.spawn_client = self.create_client(Spawn, '/spawn')

        if not self.spawn_client.wait_for_service(timeout_sec=5.0):
            self.get_logger().error('Turtlesim /spawn service not available.')
            raise RuntimeError('Missing turtlesim spawn service')

        self.center_x = 5.54
        self.center_y = 5.54
        self.radius = 2.0

    def calc_position(self, n: int, radius: float):
        """Compute circle positions for n turtles around a given radius.

        Args:
            n: Number of turtle positions to compute.
            radius: Radius of the circle around the center.

        Returns:
            Tuple of three lists: x positions, y positions, and theta angles.
        """
        if n <= 0:
            return [], [], []

        gap_theta = 2.0 * math.pi / float(n)
        theta = [gap_theta * i for i in range(n)]
        # to_degree = 180/np.pi
        # to_ radian = np.pi/180
        x = [radius * math.cos(angle) for angle in theta]
        y = [radius * math.sin(angle) for angle in theta]
        return x, y, theta

    def callback_service(self, request, response):
        """Handle MultiSpawn requests from clients.

        The service request contains a single integer 'num'. The response
        returns arrays of x, y, and theta values for the spawned turtles.
        Each turtle is spawned around the fixed center point.
        """
        self.get_logger().info(f'Received MultiSpawn request: num={request.num}')

        num_turtles = max(0, int(request.num))
        x_positions, y_positions, theta_positions = self.calc_position(
            num_turtles,
            self.radius,
        )

        for index in range(num_turtles):
            spawn_request = Spawn.Request()
            spawn_request.x = float(x_positions[index] + self.center_x)
            spawn_request.y = float(y_positions[index] + self.center_y)
            spawn_request.theta = float(theta_positions[index])
            spawn_request.name = ''  # Let turtlesim assign a default name.

            self.get_logger().info(
                f'Spawning turtle {index + 1}/{num_turtles} at '
                f'({spawn_request.x:.2f}, {spawn_request.y:.2f})'
            )
            self.spawn_client.call_async(spawn_request)
            time.sleep(0.1)

        response.x = [float(value) for value in x_positions]
        response.y = [float(value) for value in y_positions]
        response.theta = [float(value) for value in theta_positions]
        return response


def main(args=None):
    rclpy.init(args=args)
    node = MultiSpawning()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
