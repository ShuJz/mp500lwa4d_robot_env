; Auto-generated. Do not edit!


(cl:in-package robot_service-srv)


;//! \htmlinclude RLChooseAction-request.msg.html

(cl:defclass <RLChooseAction-request> (roslisp-msg-protocol:ros-message)
  ((state
    :reader state
    :initarg :state
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass RLChooseAction-request (<RLChooseAction-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RLChooseAction-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RLChooseAction-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_service-srv:<RLChooseAction-request> is deprecated: use robot_service-srv:RLChooseAction-request instead.")))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <RLChooseAction-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_service-srv:state-val is deprecated.  Use robot_service-srv:state instead.")
  (state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RLChooseAction-request>) ostream)
  "Serializes a message object of type '<RLChooseAction-request>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'state))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'state))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RLChooseAction-request>) istream)
  "Deserializes a message object of type '<RLChooseAction-request>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'state) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'state)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RLChooseAction-request>)))
  "Returns string type for a service object of type '<RLChooseAction-request>"
  "robot_service/RLChooseActionRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RLChooseAction-request)))
  "Returns string type for a service object of type 'RLChooseAction-request"
  "robot_service/RLChooseActionRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RLChooseAction-request>)))
  "Returns md5sum for a message object of type '<RLChooseAction-request>"
  "6904b829fd6bdbea4739bf92ec4b118d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RLChooseAction-request)))
  "Returns md5sum for a message object of type 'RLChooseAction-request"
  "6904b829fd6bdbea4739bf92ec4b118d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RLChooseAction-request>)))
  "Returns full string definition for message of type '<RLChooseAction-request>"
  (cl:format cl:nil "float64[] state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RLChooseAction-request)))
  "Returns full string definition for message of type 'RLChooseAction-request"
  (cl:format cl:nil "float64[] state~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RLChooseAction-request>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'state) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RLChooseAction-request>))
  "Converts a ROS message object to a list"
  (cl:list 'RLChooseAction-request
    (cl:cons ':state (state msg))
))
;//! \htmlinclude RLChooseAction-response.msg.html

(cl:defclass <RLChooseAction-response> (roslisp-msg-protocol:ros-message)
  ((action
    :reader action
    :initarg :action
    :type (cl:vector cl:float)
   :initform (cl:make-array 0 :element-type 'cl:float :initial-element 0.0)))
)

(cl:defclass RLChooseAction-response (<RLChooseAction-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RLChooseAction-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RLChooseAction-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name robot_service-srv:<RLChooseAction-response> is deprecated: use robot_service-srv:RLChooseAction-response instead.")))

(cl:ensure-generic-function 'action-val :lambda-list '(m))
(cl:defmethod action-val ((m <RLChooseAction-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader robot_service-srv:action-val is deprecated.  Use robot_service-srv:action instead.")
  (action m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RLChooseAction-response>) ostream)
  "Serializes a message object of type '<RLChooseAction-response>"
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'action))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (cl:let ((bits (roslisp-utils:encode-double-float-bits ele)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream)))
   (cl:slot-value msg 'action))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RLChooseAction-response>) istream)
  "Deserializes a message object of type '<RLChooseAction-response>"
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'action) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'action)))
    (cl:dotimes (i __ros_arr_len)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:aref vals i) (roslisp-utils:decode-double-float-bits bits))))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RLChooseAction-response>)))
  "Returns string type for a service object of type '<RLChooseAction-response>"
  "robot_service/RLChooseActionResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RLChooseAction-response)))
  "Returns string type for a service object of type 'RLChooseAction-response"
  "robot_service/RLChooseActionResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RLChooseAction-response>)))
  "Returns md5sum for a message object of type '<RLChooseAction-response>"
  "6904b829fd6bdbea4739bf92ec4b118d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RLChooseAction-response)))
  "Returns md5sum for a message object of type 'RLChooseAction-response"
  "6904b829fd6bdbea4739bf92ec4b118d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RLChooseAction-response>)))
  "Returns full string definition for message of type '<RLChooseAction-response>"
  (cl:format cl:nil "float64[] action~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RLChooseAction-response)))
  "Returns full string definition for message of type 'RLChooseAction-response"
  (cl:format cl:nil "float64[] action~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RLChooseAction-response>))
  (cl:+ 0
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'action) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ 8)))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RLChooseAction-response>))
  "Converts a ROS message object to a list"
  (cl:list 'RLChooseAction-response
    (cl:cons ':action (action msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'RLChooseAction)))
  'RLChooseAction-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'RLChooseAction)))
  'RLChooseAction-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RLChooseAction)))
  "Returns string type for a service object of type '<RLChooseAction>"
  "robot_service/RLChooseAction")