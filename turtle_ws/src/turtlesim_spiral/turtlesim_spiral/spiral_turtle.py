import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class SpiralTurtle(Node):
    def __init__(self):
        super().__init__('spiral_turtle')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)
        self.linear_velocity = 1.0  # Start with a moderate linear velocity
        self.angular_velocity = 3.0  # Start with a higher angular velocity

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = self.linear_velocity
        msg.angular.z = self.angular_velocity
        
        # Increase linear velocity more gradually to create spacing between circles
        self.linear_velocity += 0.05
        # Decrease angular velocity more gradually to widen the spiral
        self.angular_velocity -= 0.01

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    spiral_turtle = SpiralTurtle()
    rclpy.spin(spiral_turtle)
    spiral_turtle.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
