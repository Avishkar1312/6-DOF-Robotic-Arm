FROM ros:foxy-ros-base-focal

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    build-essential \
    vim nano \
    git \
    curl \
    python3-pip \
    python3-rosdep \
    python3-colcon-common-extensions \
    ros-foxy-joint-state-publisher-gui \
    ros-foxy-rviz2 \
    ros-foxy-gazebo-ros-pkgs \
    ros-foxy-moveit \
    ros-foxy-xacro \
    python3-dev \
    python3-setuptools \
    i2c-tools \
    x11-apps \
    && apt-get clean

RUN pip3 install pyserial \
    adafruit-pca9685 \
    adafruit-blinka \
    adafruit-circuitpython-servokit 

WORKDIR /home/robot_arm
COPY ./src 

RUN rosdep init || true           
RUN rosdep update

RUN /bin/bash -c "source /opt/ros/foxy/setup.bash && \
    rosdep install --from-paths src --ignore-src -r -y && \
    colcon build"

CMD ["bash"]
