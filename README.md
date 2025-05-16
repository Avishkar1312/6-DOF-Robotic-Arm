# 6-DOF Robotic Arm &#x1F916;

A robotic arm with 6 degrees of freedom made out of 3D printed parts. The software stack is primarily present in a Docker container setup in Raspberry Pi OS. It consists of a ROS2 pipeline written in Python with some C++ code in the Arduino IDE for controlling the stepper motors.

## Current Functionality:

* Currently only kinematic control has been established
* Individual joint angles can be altered using the Joint_State_Publisher_Gui and the respective changes in the configuration can be seen in the 3d model on Rviz2
* The desired joint angles can then be passed on to the hardware by pressing the "Enter" button in the GUI
* The hardware model receives the joint angles and aligns itself to match the configuration of the 3D model visualised in RViz

## Flow Chart:

<img src="./img/Robotic_arm.drawio.svg" alt="Flowchart" width="100%"/>

## Pic of the model:

![Hardware model](img/6dof_robotic_arm_1.jpeg)

## Softwares Used:

* SolidWorks
* Docker
* Raspberry Pi 5 OS
* Arduino IDE
* ROS2 Foxy
* RViz2

## Steps to replicate this identical model:

### I. CAD Model:

SolidWorks was used for creating the individual parts and assembling them together. If you want to use an identical model the cad files for all the individual parts and the assembly is present in the [Cad_files](Cad_files/) folder.

#### References used for modelling:

[RoTechnic Playlist](https://www.youtube.com/@roTechnic/playlists)

[Cycloidal Gear design](https://ewhiteowls.com/2022/02/the-ultimate-guide-to-design-cycloidal-drives-the-beating-heart-of-robotic-arms/)

[Modelling the robotic arm](https://www.youtube.com/playlist?list=PLeEzO_sX5H6TBD6EMGgV-qdhzxPY19m121)

After you have assembled it on SolidWorks, you will have to assign the proper coordinate frames to each joint(Tutorial for this is present in the references).

Once everything in  modelling is done, we will generate a URDF file for the model. For this, use the [Solidworks to URDF Converter](https://wiki.ros.org/sw_urdf_exporter) which will create a ROS package with your model in it.

We ultimately want a ROS2 package so we would use this application to convert it into a ROS2 package 

[ROS2 URDF Converter](https://wiki.ros.org/sw_urdf_exporter)

### II. Setting up Pi Environment:

Use Raspberry Pi Imager to flash the Raspberry Pi 5 OS image onto a USB drive. Then insert the USB into the Raspberry Pi 5 to boot from it
Configure the Pi accordingly. Some key configuration steps to follow:


1. Go into Raspi-Config
2. Enable SSH, VNC, and I2C
3. Enable the serial hardware port
4. Change the forwarding from Wayland to X11

#### Clone the repo:

```bash
git clone https://github.com/Avishkar1312/6-DOF-Robotic-Arm.git
```

#### Go into the folder and build the Docker image

```bash
docker build -t your-image-name .  #Keep the name according to your choice
```
### III. Running the simulation:

#### In one terminal run 

```bash
xhost +local:root
```
This command allows the root user to access the X server. This would be essential to see the GUI output of Rviz2 on the screen.

#### In another terminal, go into your work folder(in this case)

```bash
cd 6-DOF-Robotic-Arm-main 
```

#### Run the container:

> ⚠️ **Disclaimer:** Connect the Arduino with Raspberry Pi5 before running the command
```bash
docker run -it --rm --env DISPLAY=:0 --volume /tmp/.X11-unix:/tmp/.X11-unix --volume /path/on/host:/path/in/container --device /dev/ttyACM0 your_container_name
```

#### Navigate to the working directory and source the ros2 environment

```bash
source /opt/ros/foxy/setup.bash
```

#### Build the packages

```bash
colcon build 
```
This will create install,build and log folders in your workspace

#### Source the workspace 

```bash
source install/setup.bash
```
#### Launch the GUI and RViz window

```bash
ros2 launch final_arm_urdf launch.py 
```

You would now be able to interact with the simulation using the Joint_State_Publisher_GUI

### IV. Setting up the circuit connections

For the circuit diagrams, follow the images given in the [Circuit_diagrams](Circuit_diagrams/) folder. Copy the code given in the [Arduino_codes](Arduino_codes/) folder and paste it into your Arduino IDE. Upload this code into your respective Arduino.

After completing the circuit and connecting the motors, follow the further instructions to run the motor

1. Execute the steps of part III. (running the simulation) same as mentioned
2. Open a new terminal and go into the Docker container

```bash
docker ps 
```
Then copy the generated container id and use it in 

```bash
docker exec -it <container_id> bash # Paste your container id 
```

This will take you to the same container. Now navigate again to your workspace and source it. After all this, run the following command

```bash
ros2 launch raspi motor_launch.py
```
This will launch the nodes for each motor at once.

The hardware model is also ready to be executed. On pressing the "Enter" button on the GUI the specific configuration joint angles would be passed onto the hardware.

## Hardware Configuration:

| Joint | Gear type & Ratio | Motor |
|-----------------|-----------------|-----------------|
| Base Joint    | Cycloidal Gear (1:10)    | NEMA 17 Stepper motor    |
| Shoulder Joint    | Snug fit(1:3.71)    | NEMA 17 Stepper motor with gearbox    |
| Elbow Joint    | Snug Fit( Internal gears in servo)(1:1)   | Metal geared servo motor    |
| Wrist joints(3)    | Snug Fit( Internal gears in servo)(1:1)    | Plastic geared servo motor    |

## Future Work to be done:

* Dynamic control is to be added
* Thinking of venturing into upper-level control, such as voice control.

## Open for more suggestions


   




































