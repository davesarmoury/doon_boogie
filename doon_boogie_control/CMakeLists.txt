cmake_minimum_required(VERSION 3.0.2)
project(doon_boogie_control)

find_package(catkin REQUIRED COMPONENTS
  rospy
  sensor_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES doon_boogie_control
#  CATKIN_DEPENDS rospy sensor_msgs
#  DEPENDS system_lib
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)
