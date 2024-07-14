[![Choaib ELMADI - ROS](https://img.shields.io/badge/Choaib_ELMADI-ROS-8800dd)](https://elmadichoaib.vercel.app) ![Status - Learning](https://img.shields.io/badge/Status-Learning-2bd729)

# ROS: Robot Operating System

ROS is a set of software libraries and tools that help you build robot applications.

![ROS1 - ROS Noetic](https://img.shields.io/badge/ROS1_-_ROS_Noetic-fb151a?style=for-the-badge)

## Requirements

- **Operating System**: Debian-based distribution, here I used Ubuntu 20.04.6 LTS.
- **ROS Version**: ROS Noetic, latest version of ROS 1.

## ROS Noetic Installation and Setup

### 1. Make sure that your OS is installed correctly.

### 2. Setup your sources.list:

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```

### 3. Set up your keys:

```bash
sudo apt install curl
```

```bash
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```

### 4. Installation:

```bash
sudo apt update
```

#### **Desktop-Full Install (Recommended)**:

```bash
sudo apt install ros-noetic-desktop-full
```

### 5. Environment setup:

#### You must source this script in every bash terminal you use ROS in:

```bash
source /opt/ros/noetic/setup.bash
```

#### To start a ROS master, run this command:

```bash
roscore # start a ros master
```

#### In order to run multiple ROS masters in different terminals, you must source the script in every bash terminal you use ROS in, or you can just run this command for all of them:

```bash
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
```

Visit this link for more details: [Ubuntu install of ROS Noetic](https://wiki.ros.org/noetic/Installation/Ubuntu)

![ROS2 - ROS Humble](https://img.shields.io/badge/ROS2_-_ROS_Humble-fb151a?style=for-the-badge)
