#!/bin/bash
set -e

echo "========================================="
echo "   ROS 2 Jazzy Auto Installer for UTM    "
echo "========================================="

# 1. Locale 설정
echo "[1/5] 로케일 설정을 진행합니다..."
sudo apt update && sudo apt install locales -y
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

# 2. Ubuntu Universe 저장소 및 ROS 2 GPG Key 등록
echo "[2/5] ROS 2 공식 저장소를 등록합니다..."
sudo apt install software-properties-common -y
sudo add-apt-repository universe -y
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

# 3. ROS 2 Desktop 및 Gazebo Harmonic 설치
echo "[3/5] ROS 2 Jazzy Desktop 및 Gazebo를 설치합니다 (시간이 다소 소요됩니다)..."
sudo apt update
sudo apt install colcon -y
sudo apt install ros-jazzy-desktop -y
sudo apt install ros-jazzy-ros-gz -y
sudo apt install -y ros-jazzy-joint-state-publisher-gui
sudo apt install -y ros-jazzy-slam-toolbox
sudo apt install -y ros-jazzy-tf-transformations python3-transforms3d
sudo apt install -y ros-jazzy-navigation2 ros-jazzy-nav2-bringup
sudo apt install -y ros-jazzy-cv-bridge ros-jazzy-image-transport-plugins
## MoveIt 설치
sudo apt install ros-jazzy-moveit -y
sudo apt install ros-jazzy-rmw-cyclonedds-cpp -y
sudo apt install ros-jazzy-controller-manager ros-jazzy-ros2-control ros-jazzy-ros2-controllers

# export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp 



# 4. 개발 도구 및 rosdep 설정
echo "[4/5] 개발 툴 및 rosdep 초기화를 진행합니다..."
sudo apt install python3-colcon-common-extensions python3-rosdep python3-argcomplete -y
if [ ! -f /etc/ros/rosdep/sources.list.d/20-default.list ]; then
    sudo rosdep init
fi
rosdep update
sudo apt install ros-jazzy-rqt-tf-tree -y

# 5. 환경 변수 등록 (.bashrc)
echo "[5/5] 환경 변수를 .bashrc에 등록합니다..."
if ! grep -q "source /opt/ros/jazzy/setup.bash" ~/.bashrc; then
    echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
fi

echo "========================================="
echo "  설치가 완료되었습니다! 터미널을 다시 켜거나 "
echo "  'source ~/.bashrc'를 입력하여 적용하세요.   "
echo "========================================="
