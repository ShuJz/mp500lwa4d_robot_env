if(EXISTS "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libphidgets/EP_libphidgets-prefix/src/libphidget_2.1.8.20151217.tar.gz")
  file("MD5" "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libphidgets/EP_libphidgets-prefix/src/libphidget_2.1.8.20151217.tar.gz" hash_value)
  if("x${hash_value}" STREQUAL "x818ab2ff1de92ed9568a206e0e89657f")
    return()
  endif()
endif()
message(STATUS "downloading...
     src='https://www.phidgets.com/downloads/phidget21/libraries/linux/libphidget/libphidget_2.1.8.20151217.tar.gz'
     dst='/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libphidgets/EP_libphidgets-prefix/src/libphidget_2.1.8.20151217.tar.gz'
     timeout='none'")




file(DOWNLOAD
  "https://www.phidgets.com/downloads/phidget21/libraries/linux/libphidget/libphidget_2.1.8.20151217.tar.gz"
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libphidgets/EP_libphidgets-prefix/src/libphidget_2.1.8.20151217.tar.gz"
  SHOW_PROGRESS
  # no TIMEOUT
  STATUS status
  LOG log)

list(GET status 0 status_code)
list(GET status 1 status_string)

if(NOT status_code EQUAL 0)
  message(FATAL_ERROR "error: downloading 'https://www.phidgets.com/downloads/phidget21/libraries/linux/libphidget/libphidget_2.1.8.20151217.tar.gz' failed
  status_code: ${status_code}
  status_string: ${status_string}
  log: ${log}
")
endif()

message(STATUS "downloading... done")
