set(file "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libconcorde_tsp_solver/EP_libconcorde_tsp_solver-prefix/src/concorde-tsp-solver-20031219.tar.gz")
message(STATUS "verifying file...
     file='${file}'")
set(expect_value "fba5435ca1fd01f9da081fe5232a7203")
set(attempt 0)
set(succeeded 0)
while(${attempt} LESS 3 OR ${attempt} EQUAL 3 AND NOT ${succeeded})
  file(MD5 "${file}" actual_value)
  if("${actual_value}" STREQUAL "${expect_value}")
    set(succeeded 1)
  elseif(${attempt} LESS 3)
    message(STATUS "MD5 hash of ${file}
does not match expected value
  expected: ${expect_value}
    actual: ${actual_value}
Retrying download.
")
    file(REMOVE "${file}")
    execute_process(COMMAND ${CMAKE_COMMAND} -P "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/build/cob_extern/libconcorde_tsp_solver/EP_libconcorde_tsp_solver-prefix/src/EP_libconcorde_tsp_solver-stamp/download-EP_libconcorde_tsp_solver.cmake")
  endif()
  math(EXPR attempt "${attempt} + 1")
endwhile()

if(${succeeded})
  message(STATUS "verifying file... done")
else()
  message(FATAL_ERROR "error: MD5 hash of
  ${file}
does not match expected value
  expected: ${expect_value}
    actual: ${actual_value}
")
endif()
