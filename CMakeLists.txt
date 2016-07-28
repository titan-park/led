cmake_minimum_required(VERSION 2.8.3)
project(led)

find_package(catkin REQUIRED COMPONENTS
#  message_generation
  roscpp
  rospy
  std_msgs
)

#generate_messages(
#  DEPENDENCIES
#  std_msgs
#)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES led
  CATKIN_DEPENDS roscpp rospy std_msgs
#message_generation 
  DEPENDS system_lib
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
