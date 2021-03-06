# Install script for directory: /home/drcl_jetson/workspace/Jetson-xavier-slam-ws/src/mecanum_robot_pkg/openrobot_control

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/drcl_jetson/workspace/Jetson-xavier-slam-ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/openrobot_control_6omni/cmake" TYPE FILE FILES "/home/drcl_jetson/workspace/Jetson-xavier-slam-ws/build/mecanum_robot_pkg/openrobot_control/catkin_generated/installspace/openrobot_control_6omni-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/drcl_jetson/workspace/Jetson-xavier-slam-ws/devel/share/roseus/ros/openrobot_control_6omni")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python2" -m compileall "/home/drcl_jetson/workspace/Jetson-xavier-slam-ws/devel/lib/python2.7/dist-packages/openrobot_control_6omni")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/drcl_jetson/workspace/Jetson-xavier-slam-ws/devel/lib/python2.7/dist-packages/openrobot_control_6omni")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/drcl_jetson/workspace/Jetson-xavier-slam-ws/build/mecanum_robot_pkg/openrobot_control/catkin_generated/installspace/openrobot_control_6omni.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/openrobot_control_6omni/cmake" TYPE FILE FILES "/home/drcl_jetson/workspace/Jetson-xavier-slam-ws/build/mecanum_robot_pkg/openrobot_control/catkin_generated/installspace/openrobot_control_6omni-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/openrobot_control_6omni/cmake" TYPE FILE FILES
    "/home/drcl_jetson/workspace/Jetson-xavier-slam-ws/build/mecanum_robot_pkg/openrobot_control/catkin_generated/installspace/openrobot_control_6omniConfig.cmake"
    "/home/drcl_jetson/workspace/Jetson-xavier-slam-ws/build/mecanum_robot_pkg/openrobot_control/catkin_generated/installspace/openrobot_control_6omniConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/openrobot_control_6omni" TYPE FILE FILES "/home/drcl_jetson/workspace/Jetson-xavier-slam-ws/src/mecanum_robot_pkg/openrobot_control/package.xml")
endif()

