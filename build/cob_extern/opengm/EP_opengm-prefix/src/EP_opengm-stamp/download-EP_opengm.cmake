if(EXISTS "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/opengm/EP_opengm-prefix/src/opengm-master.tar.gz")
  file("MD5" "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/opengm/EP_opengm-prefix/src/opengm-master.tar.gz" hash_value)
  if("x${hash_value}" STREQUAL "x414951b2772f4ed5683a6cf6bdd6eb0d")
    return()
  endif()
endif()
message(STATUS "downloading...
     src='https://github.com/ipa320/thirdparty/raw/master/opengm-master.tar.gz'
     dst='/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/opengm/EP_opengm-prefix/src/opengm-master.tar.gz'
     timeout='none'")




file(DOWNLOAD
  "https://github.com/ipa320/thirdparty/raw/master/opengm-master.tar.gz"
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/opengm/EP_opengm-prefix/src/opengm-master.tar.gz"
  SHOW_PROGRESS
  # no TIMEOUT
  STATUS status
  LOG log)

list(GET status 0 status_code)
list(GET status 1 status_string)

if(NOT status_code EQUAL 0)
  message(FATAL_ERROR "error: downloading 'https://github.com/ipa320/thirdparty/raw/master/opengm-master.tar.gz' failed
  status_code: ${status_code}
  status_string: ${status_string}
  log: ${log}
")
endif()

message(STATUS "downloading... done")
