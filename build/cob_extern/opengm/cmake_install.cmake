# Install script for directory: /home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/cob_extern/opengm

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/opengm/catkin_generated/installspace/opengm.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/opengm/cmake" TYPE FILE FILES "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/opengm/catkin_generated/installspace/opengm-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/opengm/cmake" TYPE FILE FILES
    "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/opengm/catkin_generated/installspace/opengmConfig.cmake"
    "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/opengm/catkin_generated/installspace/opengmConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/opengm" TYPE FILE FILES "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/cob_extern/opengm/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/opengm" TYPE DIRECTORY FILES "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/devel/include/opengm/")
endif()

