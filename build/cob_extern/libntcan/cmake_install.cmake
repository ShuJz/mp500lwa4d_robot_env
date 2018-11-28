# Install script for directory: /home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/cob_extern/libntcan

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/install")
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

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libntcan/catkin_generated/installspace/libntcan.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/libntcan/cmake" TYPE FILE FILES
    "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libntcan/catkin_generated/installspace/libntcanConfig.cmake"
    "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libntcan/catkin_generated/installspace/libntcanConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/libntcan" TYPE FILE FILES "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/cob_extern/libntcan/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE PROGRAM FILES
    "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/cob_extern/libntcan/common/lib/x86_64/libntcan.so"
    "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/cob_extern/libntcan/common/lib/x86_64/libntcan.so.3"
    "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/cob_extern/libntcan/common/lib/x86_64/libntcan.so.3.1.7"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/libntcan" TYPE DIRECTORY FILES "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/cob_extern/libntcan/common/include/libntcan/")
endif()

