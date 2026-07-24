cmake_minimum_required(VERSION 3.8)
project(first_package_msgs LANGUAGES C CXX)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/CmdAndPoseVel.msg"
  "srv/MultiSpawn.srv"
)

ament_export_dependencies(rosidl_default_runtime)

ament_package()
