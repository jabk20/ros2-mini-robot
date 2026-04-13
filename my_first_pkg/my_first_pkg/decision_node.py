import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32, String

class DecisionNode(Node):

    def __init__(self):
        super().__init__('decision_node')
        self.subscription = self.create_subscription(
            Float32,
            'distance',
            self.callback,
            10
        )
        
        self.publisher_= self.create_publisher(String, 'robot_action', 10)


    def callback(self, msg):
        distance = msg.data
        action_msg = String()

        if distance < 2.0:
            action_msg.data = "STOP"
        elif distance < 5.0:
            action_msg.data = "SLOW"
        else:
            action_msg.data = "FAST"

        self.publisher_.publish(action_msg)
        self.get_logger().info(f'Action: {action_msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = DecisionNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
