from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='raspi',
            executable='stepper_node',
            name='stepper_node'
        ),

        Node(
            package='raspi',
            executable='elbow_servo_node',
            name='elbow_servo_node'
        ),

        Node(
            package='raspi',
            executable='wrist_roll_node',
            name='wrist_roll_node'
        ),
        
        Node(
            package='raspi',
            executable='wrist_pitch_node',
            name='wrist_pitch_node'
        ),
        
        Node(
            package='raspi',
            executable='wrist_yaw_node',
            name='wrist_yaw_node'
        ),
    ])
