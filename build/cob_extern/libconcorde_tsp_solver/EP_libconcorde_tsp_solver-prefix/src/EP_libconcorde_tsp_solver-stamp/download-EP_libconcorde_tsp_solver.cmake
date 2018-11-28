if(EXISTS "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libconcorde_tsp_solver/EP_libconcorde_tsp_solver-prefix/src/concorde-tsp-solver-20031219.tar.gz")
  file("MD5" "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libconcorde_tsp_solver/EP_libconcorde_tsp_solver-prefix/src/concorde-tsp-solver-20031219.tar.gz" hash_value)
  if("x${hash_value}" STREQUAL "xfba5435ca1fd01f9da081fe5232a7203")
    return()
  endif()
endif()
message(STATUS "downloading...
     src='https://github.com/ipa320/thirdparty/raw/master/concorde-tsp-solver-20031219.tar.gz'
     dst='/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libconcorde_tsp_solver/EP_libconcorde_tsp_solver-prefix/src/concorde-tsp-solver-20031219.tar.gz'
     timeout='none'")




file(DOWNLOAD
  "https://github.com/ipa320/thirdparty/raw/master/concorde-tsp-solver-20031219.tar.gz"
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libconcorde_tsp_solver/EP_libconcorde_tsp_solver-prefix/src/concorde-tsp-solver-20031219.tar.gz"
  SHOW_PROGRESS
  # no TIMEOUT
  STATUS status
  LOG log)

list(GET status 0 status_code)
list(GET status 1 status_string)

if(NOT status_code EQUAL 0)
  message(FATAL_ERROR "error: downloading 'https://github.com/ipa320/thirdparty/raw/master/concorde-tsp-solver-20031219.tar.gz' failed
  status_code: ${status_code}
  status_string: ${status_string}
  log: ${log}
")
endif()

message(STATUS "downloading... done")
