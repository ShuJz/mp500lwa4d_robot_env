# Install script for directory: /home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/cob_extern/libconcorde_tsp_solver

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libconcorde_tsp_solver/catkin_generated/installspace/libconcorde_tsp_solver.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/libconcorde_tsp_solver/cmake" TYPE FILE FILES "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libconcorde_tsp_solver/catkin_generated/installspace/libconcorde_tsp_solver-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/libconcorde_tsp_solver/cmake" TYPE FILE FILES
    "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libconcorde_tsp_solver/catkin_generated/installspace/libconcorde_tsp_solverConfig.cmake"
    "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libconcorde_tsp_solver/catkin_generated/installspace/libconcorde_tsp_solverConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/libconcorde_tsp_solver" TYPE FILE FILES "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/cob_extern/libconcorde_tsp_solver/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/libconcorde_tsp_solver" TYPE DIRECTORY FILES "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/devel/include/libconcorde_tsp_solver/")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE FILE FILES "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/devel/lib/concorde.a")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/libconcorde_tsp_solver" TYPE PROGRAM FILES "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/devel/lib/libconcorde_tsp_solver/concorde")
endif()

