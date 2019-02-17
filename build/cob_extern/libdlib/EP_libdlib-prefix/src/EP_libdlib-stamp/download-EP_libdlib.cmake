if(EXISTS "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libdlib/EP_libdlib-prefix/src/dlib-18.17.tar.bz2")
  file("MD5" "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libdlib/EP_libdlib-prefix/src/dlib-18.17.tar.bz2" hash_value)
  if("x${hash_value}" STREQUAL "x249164604423590c3f1682ab1af66ca0")
    return()
  endif()
endif()
message(STATUS "downloading...
     src='https://github.com/ipa320/thirdparty/raw/master/dlib-18.17.tar.bz2'
     dst='/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libdlib/EP_libdlib-prefix/src/dlib-18.17.tar.bz2'
     timeout='none'")




file(DOWNLOAD
  "https://github.com/ipa320/thirdparty/raw/master/dlib-18.17.tar.bz2"
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libdlib/EP_libdlib-prefix/src/dlib-18.17.tar.bz2"
  SHOW_PROGRESS
  # no TIMEOUT
  STATUS status
  LOG log)

list(GET status 0 status_code)
list(GET status 1 status_string)

if(NOT status_code EQUAL 0)
  message(FATAL_ERROR "error: downloading 'https://github.com/ipa320/thirdparty/raw/master/dlib-18.17.tar.bz2' failed
  status_code: ${status_code}
  status_string: ${status_string}
  log: ${log}
")
endif()

message(STATUS "downloading... done")
