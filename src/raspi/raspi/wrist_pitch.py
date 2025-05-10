import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from Adafruit_PCA9685 import PCA9685
#from adafruit_servokit import ServoKit
from time import sleep


class Servo_Subscriber(Node):
    def __init__(self):
        super().__init__('servo_subscriber')
        #self.kit =ServoKit(channels=16)
        self.get_logger().info("Initializing PCA9685")
        self.pwm=PCA9685(busnum=1)
        self.pwm.set_pwm_freq(60)
        self.get_logger().info("PCA9685 Initialized. Freq set to 60Hz")
        self.servo_subscriber=self.create_subscription(JointState,'/robo_angles',self.timer_callback,10)
        self.servo_subscriber


    def timer_callback(self,msg):
        desired_wrist_pitch_angle=msg.position[3]*180/3.14
        #=msg.position[4]*180/3.14
        #desired_wrist_yaw_angle=msg.position[5]*180/3.14
        pulse = self.angle_to_pulse(desired_wrist_pitch_angle)
        self.pwm.set_pwm(1, 0, pulse)
        self.get_logger().info("Servo moved")
        """
#print(f"Servo moved to {desired_wrist_roll_angle} degrees and stopped")
        pulse = self.angle_to_pulse(desired_wrist_pitch_angle)
        self.pwm.set_pwm(2, 0, pulse)
        self.get_logger().info("Servo moved")
 #       print(f"Servo moved to {desired_wrist_pitch_angle} degrees and stopped")
        #pulse = angle_to_pulse(desired_wrist_yaw_angle)
        #self.pwm.set_pwm(3, 0, pulse)
        #self.get_logger().info("Servo moved")
  #      print(f"Servo moved to {desired_wrist_yaw_angle} degrees and stopped.")
"""

    def angle_to_pulse(self,angle):
        pulse= int (375+(angle /90.0)*225)
        return max(150, min(pulse,600))

def main(args=None):
    rclpy.init(args=args)
    node=Servo_Subscriber()
    rclpy.spin(node)
    rclpy.shutdown()
        

