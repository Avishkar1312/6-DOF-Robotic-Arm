import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import serial
import time

class Stepper_subscriber(Node):
    def __init__(self):
        super().__init__('jstepper_subscriber')

        self.arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        time.sleep(2)
        self.stepper=self.create_subscription(JointState,'/robo_angles',self.timer_callback,10)
        self.stepper
 

    def timer_callback(self,msg):
        
        base_angle=msg.position[0]
        base_speed=300
        shoulder_angle=msg.position[1]
        shoulder_speed=150
        stepper_cmd=f"{base_angle} {base_speed} {shoulder_angle} {shoulder_speed}\n"
        self.arduino.write(stepper_cmd.encode())
        self.get_logger().info("Sent to Arduino: %s" % stepper_cmd.strip())

        while True:
            if self.arduino.in_waiting:
                updates=self.arduino.readline().decode().strip()
                self.get_logger().info("Arduino: %s" %updates)
                if "done" == updates.lower():
                    break


        #self.get_logger().info("Base: %d" %msg.position[0])


def main(args=None):
    rclpy.init(args=args)
    node=Stepper_subscriber()
    rclpy.spin(node)
    node.arduino.close()
    rclpy.shutdown()


