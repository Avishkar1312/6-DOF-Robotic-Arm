# 6-DOF Robotic Arm &#x1F916;

A robotic arm with 6 degrees of freedom made out of 3d printed parts. The software stack is primarily present in a Docker container setup in Raspberry Pi OS. Its software side consists of a ROS2 pipeline written in Python with some C++ code in the Arduino IDE for controlling the stepper motors.

## Current Functionality:

* Individual joint angles can be altered using the Joint_State_Publisher_Gui and the respective changes in the configuration can be seen in the 3d model on Rviz2
* The desired joint angles can then be passed on to the hardware by pressing the "Enter" button in the GUI
* The hardware model receives the joint angles and aligns itself to match the configuration of the 3D model visualised in RViz

## Pic of the model:

![Hardware model](img/6dof_robotic_arm_1.jpeg)

## Softwares Used:

* SolidWorks
* Docker
* Raspberry Pi 5 OS
* Arduino IDE
* ROS2 Foxy
* RViz2

## Steps to replicate an identical model:

### I. CAD Model:

SolidWorks was used for creating the individual parts and assembling them together. If you want to use an identical model the cad files for all the individual parts and the assembly is present in the [Cad_files](Cad_files/) folder.

#### References used for modelling:

[RoTechnic Playlist](https://www.youtube.com/@roTechnic/playlists)

[Cycloidal Gear design](https://ewhiteowls.com/2022/02/the-ultimate-guide-to-design-cycloidal-drives-the-beating-heart-of-robotic-arms/)

### II. Setting up Raspi5 Env:

Boot the raspi5 OS into the raspi by cloning the image into an usb. The image can be cloned into an usb by using [RaspberryPi Imager](https://www.raspberrypi.com/software/).
Configure the Pi accordingly. Some key configuration steps to follow:


1. Go into Raspi-Config
2. Enable SSH, VNC, and I2C
3. Enable the serial hardware port
4. Change the forwarding from Wayland to X11

Clone the repo:

```bash
git clone https://github.com/Avishkar1312/6-DOF-Robotic-Arm.git
```

Go into the folder and build the Docker image

```bash
docker build -t your-image-name .  #Keep the name according to your choice
```
### III. Running the simulation:

In one terminal run 

```bash
xhost +local:root
```
This command allows the root user to access the X server. This would be essential to see the GUI output of Rviz2 on the screen.

In another terminal, go into your work folder(in this case)

```bash
cd 6-DOF-Robotic-Arm-main 
```

Run the container:

> ⚠️ **Disclaimer:** Connect the Arduino with Raspberry Pi5 before running the command
```bash
docker run -it --rm --env DISPLAY=:0 --volume /tmp/.X11-unix:/tmp/.X11-unix --volume /path/on/host:/path/in/container --device /dev/ttyACM0 your_container_name
```

Navigate to the working directory and source the ros2 environment

```bash
source /opt/ros/foxy/setup.bash
```

Build the packages

```bash
colcon build 
```

Source the workspace 

```bash
source install/setup.bash
```
Launch the GUI and RViz window

```bash
ros2 launch final_arm_urdf launch.py 
```

You would now be able to interact with the simulation using the Joint_State_Publisher_GUI

### IV. Setting up the circuit connections

For the circuit diagrams follow the images given in the [Circuit_diagrams](Circuit_diagrams/) folder. After completing the circuit and connecting the motors , follow the further intsructiuons to run the motor




































