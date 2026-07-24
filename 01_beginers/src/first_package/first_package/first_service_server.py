import rclpy
from rclpy.node import Node

from first_package_msgs.srv import MultiSpawn


class MultiSpawning(Node):
	def __init__(self):
		super().__init__('multi_spawner')
		self.srv = self.create_service(MultiSpawn, 'multi_spawn', self.callback_service)
		self.get_logger().info('MultiSpawn service ready.')

	def callback_service(self, request, response):
		self.get_logger().info(f'Received MultiSpawn request: num={request.num}')
		n = max(0, int(request.num))
		# Example: generate simple coordinates and zero orientations
		response.x = [float(i) for i in range(n)]
		response.y = [float(i + 0.5) for i in range(n)]
		response.theta = [0.0 for _ in range(n)]
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