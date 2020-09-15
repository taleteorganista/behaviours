# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "lattepanda_behaviours: 1 messages, 0 services")

set(MSG_I_FLAGS "-Ilattepanda_behaviours:/home/lattepanda/lattepanda_behaviours/behaviour_ros/src/lattepanda_behaviours/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg;-Ilattepanda_behaviours:/home/lattepanda/lattepanda_behaviours/behaviour_ros/src/lattepanda_behaviours/msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(lattepanda_behaviours_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/lattepanda/lattepanda_behaviours/behaviour_ros/src/lattepanda_behaviours/msg/vect_msg.msg" NAME_WE)
add_custom_target(_lattepanda_behaviours_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "lattepanda_behaviours" "/home/lattepanda/lattepanda_behaviours/behaviour_ros/src/lattepanda_behaviours/msg/vect_msg.msg" "std_msgs/Header"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(lattepanda_behaviours
  "/home/lattepanda/lattepanda_behaviours/behaviour_ros/src/lattepanda_behaviours/msg/vect_msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lattepanda_behaviours
)

### Generating Services

### Generating Module File
_generate_module_cpp(lattepanda_behaviours
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lattepanda_behaviours
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(lattepanda_behaviours_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(lattepanda_behaviours_generate_messages lattepanda_behaviours_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lattepanda/lattepanda_behaviours/behaviour_ros/src/lattepanda_behaviours/msg/vect_msg.msg" NAME_WE)
add_dependencies(lattepanda_behaviours_generate_messages_cpp _lattepanda_behaviours_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lattepanda_behaviours_gencpp)
add_dependencies(lattepanda_behaviours_gencpp lattepanda_behaviours_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lattepanda_behaviours_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(lattepanda_behaviours
  "/home/lattepanda/lattepanda_behaviours/behaviour_ros/src/lattepanda_behaviours/msg/vect_msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lattepanda_behaviours
)

### Generating Services

### Generating Module File
_generate_module_eus(lattepanda_behaviours
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lattepanda_behaviours
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(lattepanda_behaviours_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(lattepanda_behaviours_generate_messages lattepanda_behaviours_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lattepanda/lattepanda_behaviours/behaviour_ros/src/lattepanda_behaviours/msg/vect_msg.msg" NAME_WE)
add_dependencies(lattepanda_behaviours_generate_messages_eus _lattepanda_behaviours_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lattepanda_behaviours_geneus)
add_dependencies(lattepanda_behaviours_geneus lattepanda_behaviours_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lattepanda_behaviours_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(lattepanda_behaviours
  "/home/lattepanda/lattepanda_behaviours/behaviour_ros/src/lattepanda_behaviours/msg/vect_msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lattepanda_behaviours
)

### Generating Services

### Generating Module File
_generate_module_lisp(lattepanda_behaviours
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lattepanda_behaviours
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(lattepanda_behaviours_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(lattepanda_behaviours_generate_messages lattepanda_behaviours_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lattepanda/lattepanda_behaviours/behaviour_ros/src/lattepanda_behaviours/msg/vect_msg.msg" NAME_WE)
add_dependencies(lattepanda_behaviours_generate_messages_lisp _lattepanda_behaviours_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lattepanda_behaviours_genlisp)
add_dependencies(lattepanda_behaviours_genlisp lattepanda_behaviours_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lattepanda_behaviours_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(lattepanda_behaviours
  "/home/lattepanda/lattepanda_behaviours/behaviour_ros/src/lattepanda_behaviours/msg/vect_msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lattepanda_behaviours
)

### Generating Services

### Generating Module File
_generate_module_nodejs(lattepanda_behaviours
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lattepanda_behaviours
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(lattepanda_behaviours_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(lattepanda_behaviours_generate_messages lattepanda_behaviours_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lattepanda/lattepanda_behaviours/behaviour_ros/src/lattepanda_behaviours/msg/vect_msg.msg" NAME_WE)
add_dependencies(lattepanda_behaviours_generate_messages_nodejs _lattepanda_behaviours_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lattepanda_behaviours_gennodejs)
add_dependencies(lattepanda_behaviours_gennodejs lattepanda_behaviours_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lattepanda_behaviours_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(lattepanda_behaviours
  "/home/lattepanda/lattepanda_behaviours/behaviour_ros/src/lattepanda_behaviours/msg/vect_msg.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/noetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lattepanda_behaviours
)

### Generating Services

### Generating Module File
_generate_module_py(lattepanda_behaviours
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lattepanda_behaviours
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(lattepanda_behaviours_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(lattepanda_behaviours_generate_messages lattepanda_behaviours_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/lattepanda/lattepanda_behaviours/behaviour_ros/src/lattepanda_behaviours/msg/vect_msg.msg" NAME_WE)
add_dependencies(lattepanda_behaviours_generate_messages_py _lattepanda_behaviours_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(lattepanda_behaviours_genpy)
add_dependencies(lattepanda_behaviours_genpy lattepanda_behaviours_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS lattepanda_behaviours_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lattepanda_behaviours)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/lattepanda_behaviours
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(lattepanda_behaviours_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET lattepanda_behaviours_generate_messages_cpp)
  add_dependencies(lattepanda_behaviours_generate_messages_cpp lattepanda_behaviours_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lattepanda_behaviours)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/lattepanda_behaviours
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(lattepanda_behaviours_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET lattepanda_behaviours_generate_messages_eus)
  add_dependencies(lattepanda_behaviours_generate_messages_eus lattepanda_behaviours_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lattepanda_behaviours)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/lattepanda_behaviours
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(lattepanda_behaviours_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET lattepanda_behaviours_generate_messages_lisp)
  add_dependencies(lattepanda_behaviours_generate_messages_lisp lattepanda_behaviours_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lattepanda_behaviours)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/lattepanda_behaviours
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(lattepanda_behaviours_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET lattepanda_behaviours_generate_messages_nodejs)
  add_dependencies(lattepanda_behaviours_generate_messages_nodejs lattepanda_behaviours_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lattepanda_behaviours)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lattepanda_behaviours\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/lattepanda_behaviours
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(lattepanda_behaviours_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET lattepanda_behaviours_generate_messages_py)
  add_dependencies(lattepanda_behaviours_generate_messages_py lattepanda_behaviours_generate_messages_py)
endif()
