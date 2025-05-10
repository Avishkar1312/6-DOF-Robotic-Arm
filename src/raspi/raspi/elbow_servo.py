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
        current_elbow_angle=0
        desired_elbow_angle=msg.position[2]*180/3.14
        i=0
        step=2 if desired_elbow_angle >=0 else -5
        for angle in range (int(current_elbow_angle), int(desired_elbow_angle -current_elbow_angle)+step,step):
            self.pwm.set_pwm(0,0, self.angle_to_pulse(angle))
            sleep(0.02)
        self.pwm.set_pwm(0,0,0)
        current_elbow_angle=desired_elbow_angle
        self.get_logger().info("Servo moved successfully")
        """
        wrist_angle_roll=msg.position[3]
        wrist_angle_pitch=msg.position[4]
        wrist_angle_yaw=msg.position[5]
        """
        #self.get_logger().info("Hello")

    def angle_to_pulse(self,angle):
        pulse= int (375+(angle /90.0)*225)
        return max(150, min(pulse,600))

def main(args=None):
    rclpy.init(args=args)
    node=Servo_Subscriber()
    rclpy.spin(node)
    rclpy.shutdown()
        

