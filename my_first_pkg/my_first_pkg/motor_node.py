import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class MotorNode(Node):

    def __init__(self):
        super().__init__('motor_node')
        self.subscription = self.create_subscription(
            String,
            'robot_action',
            self.callback,
            10
        )
        
        self.publisher_=self.create_publisher(Twist, 'cmd_vel', 10)

    def callback(self, msg):
        action = msg.data
        twist = Twist()

        if action == "STOP":
            twist.linear.x = 0.0
        elif action == "SLOW":
            twist.linear.x = 0.5
        elif action == "FAST":
            twist.linear.x = 1.0

        self.publisher_.publish(twist)
        self.get_logger().info(f'Publishing velocity: {twist.linear.x}')

def main(args=None):
    rclpy.init(args=args)
    node = MotorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
