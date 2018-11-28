if(EXISTS "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libpcan/EP_libpcan-prefix/src/peak-linux-driver-8.3.tar.gz")
  file("MD5" "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libpcan/EP_libpcan-prefix/src/peak-linux-driver-8.3.tar.gz" hash_value)
  if("x${hash_value}" STREQUAL "xd8d58223c1b1c03b891aa43763fec2cb")
    return()
  endif()
endif()
message(STATUS "downloading...
     src='http://www.peak-system.com/fileadmin/media/linux/files/peak-linux-driver-8.3.tar.gz'
     dst='/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libpcan/EP_libpcan-prefix/src/peak-linux-driver-8.3.tar.gz'
     timeout='none'")




file(DOWNLOAD
  "http://www.peak-system.com/fileadmin/media/linux/files/peak-linux-driver-8.3.tar.gz"
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libpcan/EP_libpcan-prefix/src/peak-linux-driver-8.3.tar.gz"
  SHOW_PROGRESS
  # no TIMEOUT
  STATUS status
  LOG log)

list(GET status 0 status_code)
list(GET status 1 status_string)

if(NOT status_code EQUAL 0)
  message(FATAL_ERROR "error: downloading 'http://www.peak-system.com/fileadmin/media/linux/files/peak-linux-driver-8.3.tar.gz' failed
  status_code: ${status_code}
  status_string: ${status_string}
  log: ${log}
")
endif()

message(STATUS "downloading... done")
