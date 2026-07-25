import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node
from first_package_msgs.action import MoveDistance

class MoveDistanceActionServer(Node):
    def __init__(self):
        super().__init__('move_distance_action_server')
        self._action_server = ActionServer(
            self,
            MoveDistance,
            'move_distance',
            execute_callback=self.execute_callback,
        )

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal for MoveDistance action')

        result = MoveDistance.Result()
        goal_handle.succeed()
        return result


def main(args=None):
    rclpy.init(args=args)
    move_distance_action_server = MoveDistanceActionServer()
    rclpy.spin(move_distance_action_server)
    move_distance_action_server.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
