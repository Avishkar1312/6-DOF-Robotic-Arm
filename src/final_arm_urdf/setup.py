from setuptools import setup
from glob import glob

package_name = 'final_arm_urdf'

setup(
    name=package_name,
    version='0.0.0',
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, glob('launch/*.py')),
        ('share/' + package_name+'/urdf/', glob('urdf/*')),
        ('share/' + package_name+'/rviz/', glob('rviz/*')),
        ('share/' + package_name+'/meshes/collision/', glob('meshes/collision/*')),
        ('share/' + package_name+'/meshes/visual/', glob('meshes/visual/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros-industrial',
    maintainer_email='TODO:',
    description='TODO: Package description',
    license='TODO: License declaration',
    entry_points={
        'console_scripts': [
            'joint_state_publisher_gui_custom = joint_state_publisher_gui_custom.joint_state_publisher_gui:main',
        ],
    },
)
