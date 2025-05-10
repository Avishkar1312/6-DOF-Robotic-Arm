from setuptools import setup

package_name = 'raspi'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/motor_launch.py']),
    ],
    install_requires=['setuptools',
                      #'adafruit-circuitpython-servokit',
                      #'adafruit-circuitpython-pca9685',
                      #'pyserial',
                      ],
    zip_safe=True,
    maintainer='avishkar',
    maintainer_email='aavishkar.tl@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'stepper_node = raspi.stepper:main',
            'elbow_servo_node = raspi.elbow_servo:main',
            'wrist_roll_node = raspi.wrist_roll:main',
            'wrist_pitch_node = raspi.wrist_pitch:main',
            'wrist_yaw_node = raspi.wrist_yaw:main',
        ],
    },
)
