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

```bash
sudo apt upgrade
```

#### **Desktop-Full Install (Recommended)**:

```bash
sudo apt install ros-noetic-desktop-full
```

### 5. Environment setup:

#### In order to run ROS in different terminals, you must source the setup script in every bash terminal you use ROS in. You can do this manually in each terminal, using this command:

```bash
source /opt/ros/noetic/setup.bash
```

#### Or you can add the command to your `.bashrc` file so that it is sourced automatically in every new terminal:

```bash
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
```

Visit this link for more details: [Ubuntu install of ROS Noetic](https://wiki.ros.org/noetic/Installation/Ubuntu)

![ROS2 - ROS Foxy Fitzroy](https://img.shields.io/badge/ROS2_-_ROS_Foxy_Fitzroy-fb151a?style=for-the-badge)

## Requirements

- **Operating System**: Debian-based distribution, here I used Ubuntu 20.04.6 LTS.
- **ROS Version**: ROS Foxy Fitzroy, a version of ROS 2.

## ROS Foxy Installation and Setup

### 1. Make sure that your OS is installed correctly.

### 2. Set locale:

```bash
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings
```

### 3. Setup sources:

```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```

```bash
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

### 4. Installation:

```bash
sudo apt update
```

```bash
sudo apt upgrade
```

#### **Desktop-Full Install (Recommended)**:

```bash
sudo apt install ros-foxy-desktop python3-argcomplete
```

#### **Development tools**:

```bash
sudo apt install ros-dev-tools
```

### 5. Environment setup:

#### In order to run ROS in different terminals, you must source the setup script in every bash terminal you use ROS in. You can do this manually in each terminal, using this command:

```bash
source /opt/ros/foxy/setup.bash
```

#### Or you can add the command to your `.bashrc` file so that it is sourced automatically in every new terminal:

```bash
echo "source /opt/ros/foxy/setup.bash" >> ~/.bashrc
```

Visit this link for more details: [Ubuntu install of ROS Foxy Fitzroy](https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html)
