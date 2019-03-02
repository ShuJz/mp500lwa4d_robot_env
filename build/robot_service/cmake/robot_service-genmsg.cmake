# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "robot_service: 7 messages, 2 services")

set(MSG_I_FLAGS "-Irobot_service:/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(robot_service_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/ModelStates.msg" NAME_WE)
add_custom_target(_robot_service_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot_service" "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/ModelStates.msg" "geometry_msgs/Quaternion:geometry_msgs/Pose:geometry_msgs/Twist:geometry_msgs/Point:geometry_msgs/Vector3"
)

get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/LinkState.msg" NAME_WE)
add_custom_target(_robot_service_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot_service" "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/LinkState.msg" "geometry_msgs/Quaternion:geometry_msgs/Pose:geometry_msgs/Twist:geometry_msgs/Point:geometry_msgs/Vector3"
)

get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/GetModelState.srv" NAME_WE)
add_custom_target(_robot_service_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot_service" "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/GetModelState.srv" "geometry_msgs/Twist:std_msgs/Header:geometry_msgs/Quaternion:geometry_msgs/Vector3:geometry_msgs/Point:geometry_msgs/Pose"
)

get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Twist.msg" NAME_WE)
add_custom_target(_robot_service_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot_service" "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Twist.msg" "robot_service/Vector3"
)

get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Point.msg" NAME_WE)
add_custom_target(_robot_service_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot_service" "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Point.msg" ""
)

get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Pose.msg" NAME_WE)
add_custom_target(_robot_service_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot_service" "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Pose.msg" "robot_service/Quaternion:robot_service/Point"
)

get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/RLMemoryStore.msg" NAME_WE)
add_custom_target(_robot_service_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot_service" "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/RLMemoryStore.msg" ""
)

get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Quaternion.msg" NAME_WE)
add_custom_target(_robot_service_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot_service" "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Quaternion.msg" ""
)

get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/RLChooseAction.srv" NAME_WE)
add_custom_target(_robot_service_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "robot_service" "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/RLChooseAction.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/ModelStates.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_service
)
_generate_msg_cpp(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/LinkState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_service
)
_generate_msg_cpp(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Twist.msg"
  "${MSG_I_FLAGS}"
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_service
)
_generate_msg_cpp(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Point.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_service
)
_generate_msg_cpp(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Pose.msg"
  "${MSG_I_FLAGS}"
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Quaternion.msg;/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_service
)
_generate_msg_cpp(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/RLMemoryStore.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_service
)
_generate_msg_cpp(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Quaternion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_service
)

### Generating Services
_generate_srv_cpp(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/RLChooseAction.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_service
)
_generate_srv_cpp(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/GetModelState.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_service
)

### Generating Module File
_generate_module_cpp(robot_service
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_service
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(robot_service_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(robot_service_generate_messages robot_service_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/ModelStates.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_cpp _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/LinkState.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_cpp _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/GetModelState.srv" NAME_WE)
add_dependencies(robot_service_generate_messages_cpp _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Twist.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_cpp _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Point.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_cpp _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Pose.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_cpp _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/RLMemoryStore.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_cpp _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Quaternion.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_cpp _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/RLChooseAction.srv" NAME_WE)
add_dependencies(robot_service_generate_messages_cpp _robot_service_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robot_service_gencpp)
add_dependencies(robot_service_gencpp robot_service_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robot_service_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/ModelStates.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_service
)
_generate_msg_eus(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/LinkState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_service
)
_generate_msg_eus(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Twist.msg"
  "${MSG_I_FLAGS}"
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_service
)
_generate_msg_eus(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Point.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_service
)
_generate_msg_eus(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Pose.msg"
  "${MSG_I_FLAGS}"
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Quaternion.msg;/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_service
)
_generate_msg_eus(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/RLMemoryStore.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_service
)
_generate_msg_eus(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Quaternion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_service
)

### Generating Services
_generate_srv_eus(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/RLChooseAction.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_service
)
_generate_srv_eus(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/GetModelState.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_service
)

### Generating Module File
_generate_module_eus(robot_service
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_service
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(robot_service_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(robot_service_generate_messages robot_service_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/ModelStates.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_eus _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/LinkState.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_eus _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/GetModelState.srv" NAME_WE)
add_dependencies(robot_service_generate_messages_eus _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Twist.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_eus _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Point.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_eus _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Pose.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_eus _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/RLMemoryStore.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_eus _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Quaternion.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_eus _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/RLChooseAction.srv" NAME_WE)
add_dependencies(robot_service_generate_messages_eus _robot_service_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robot_service_geneus)
add_dependencies(robot_service_geneus robot_service_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robot_service_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/ModelStates.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_service
)
_generate_msg_lisp(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/LinkState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_service
)
_generate_msg_lisp(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Twist.msg"
  "${MSG_I_FLAGS}"
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_service
)
_generate_msg_lisp(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Point.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_service
)
_generate_msg_lisp(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Pose.msg"
  "${MSG_I_FLAGS}"
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Quaternion.msg;/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_service
)
_generate_msg_lisp(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/RLMemoryStore.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_service
)
_generate_msg_lisp(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Quaternion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_service
)

### Generating Services
_generate_srv_lisp(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/RLChooseAction.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_service
)
_generate_srv_lisp(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/GetModelState.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_service
)

### Generating Module File
_generate_module_lisp(robot_service
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_service
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(robot_service_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(robot_service_generate_messages robot_service_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/ModelStates.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_lisp _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/LinkState.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_lisp _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/GetModelState.srv" NAME_WE)
add_dependencies(robot_service_generate_messages_lisp _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Twist.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_lisp _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Point.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_lisp _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Pose.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_lisp _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/RLMemoryStore.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_lisp _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Quaternion.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_lisp _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/RLChooseAction.srv" NAME_WE)
add_dependencies(robot_service_generate_messages_lisp _robot_service_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robot_service_genlisp)
add_dependencies(robot_service_genlisp robot_service_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robot_service_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/ModelStates.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_service
)
_generate_msg_nodejs(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/LinkState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_service
)
_generate_msg_nodejs(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Twist.msg"
  "${MSG_I_FLAGS}"
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_service
)
_generate_msg_nodejs(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Point.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_service
)
_generate_msg_nodejs(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Pose.msg"
  "${MSG_I_FLAGS}"
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Quaternion.msg;/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_service
)
_generate_msg_nodejs(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/RLMemoryStore.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_service
)
_generate_msg_nodejs(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Quaternion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_service
)

### Generating Services
_generate_srv_nodejs(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/RLChooseAction.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_service
)
_generate_srv_nodejs(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/GetModelState.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_service
)

### Generating Module File
_generate_module_nodejs(robot_service
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_service
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(robot_service_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(robot_service_generate_messages robot_service_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/ModelStates.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_nodejs _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/LinkState.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_nodejs _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/GetModelState.srv" NAME_WE)
add_dependencies(robot_service_generate_messages_nodejs _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Twist.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_nodejs _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Point.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_nodejs _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Pose.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_nodejs _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/RLMemoryStore.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_nodejs _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Quaternion.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_nodejs _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/RLChooseAction.srv" NAME_WE)
add_dependencies(robot_service_generate_messages_nodejs _robot_service_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robot_service_gennodejs)
add_dependencies(robot_service_gennodejs robot_service_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robot_service_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/ModelStates.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_service
)
_generate_msg_py(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/LinkState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_service
)
_generate_msg_py(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Twist.msg"
  "${MSG_I_FLAGS}"
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Vector3.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_service
)
_generate_msg_py(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Point.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_service
)
_generate_msg_py(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Pose.msg"
  "${MSG_I_FLAGS}"
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Quaternion.msg;/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_service
)
_generate_msg_py(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/RLMemoryStore.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_service
)
_generate_msg_py(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Quaternion.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_service
)

### Generating Services
_generate_srv_py(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/RLChooseAction.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_service
)
_generate_srv_py(robot_service
  "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/GetModelState.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Twist.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Vector3.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_service
)

### Generating Module File
_generate_module_py(robot_service
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_service
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(robot_service_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(robot_service_generate_messages robot_service_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/ModelStates.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_py _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/LinkState.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_py _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/GetModelState.srv" NAME_WE)
add_dependencies(robot_service_generate_messages_py _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Twist.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_py _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Point.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_py _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Pose.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_py _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/RLMemoryStore.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_py _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/msg/Quaternion.msg" NAME_WE)
add_dependencies(robot_service_generate_messages_py _robot_service_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/jingzhe/WorkSpace/ROS/mp500lwa4d_robot_env/src/robot_service/srv/RLChooseAction.srv" NAME_WE)
add_dependencies(robot_service_generate_messages_py _robot_service_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(robot_service_genpy)
add_dependencies(robot_service_genpy robot_service_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS robot_service_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_service)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/robot_service
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(robot_service_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(robot_service_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_service)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/robot_service
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(robot_service_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(robot_service_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_service)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/robot_service
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(robot_service_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(robot_service_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_service)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/robot_service
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(robot_service_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(robot_service_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_service)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_service\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/robot_service
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(robot_service_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(robot_service_generate_messages_py geometry_msgs_generate_messages_py)
endif()
