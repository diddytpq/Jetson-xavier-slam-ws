; Auto-generated. Do not edit!


(cl:in-package openrobot_vesc_msgs-msg)


;//! \htmlinclude VescStateStamped.msg.html

(cl:defclass <VescStateStamped> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (state
    :reader state
    :initarg :state
    :type openrobot_vesc_msgs-msg:VescState
    :initform (cl:make-instance 'openrobot_vesc_msgs-msg:VescState)))
)

(cl:defclass VescStateStamped (<VescStateStamped>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <VescStateStamped>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'VescStateStamped)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name openrobot_vesc_msgs-msg:<VescStateStamped> is deprecated: use openrobot_vesc_msgs-msg:VescStateStamped instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <VescStateStamped>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader openrobot_vesc_msgs-msg:header-val is deprecated.  Use openrobot_vesc_msgs-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'state-val :lambda-list '(m))
(cl:defmethod state-val ((m <VescStateStamped>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader openrobot_vesc_msgs-msg:state-val is deprecated.  Use openrobot_vesc_msgs-msg:state instead.")
  (state m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <VescStateStamped>) ostream)
  "Serializes a message object of type '<VescStateStamped>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'state) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <VescStateStamped>) istream)
  "Deserializes a message object of type '<VescStateStamped>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'state) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<VescStateStamped>)))
  "Returns string type for a message object of type '<VescStateStamped>"
  "openrobot_vesc_msgs/VescStateStamped")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'VescStateStamped)))
  "Returns string type for a message object of type 'VescStateStamped"
  "openrobot_vesc_msgs/VescStateStamped")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<VescStateStamped>)))
  "Returns md5sum for a message object of type '<VescStateStamped>"
  "9a8702668689b68c9f5537e770e374de")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'VescStateStamped)))
  "Returns md5sum for a message object of type 'VescStateStamped"
  "9a8702668689b68c9f5537e770e374de")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<VescStateStamped>)))
  "Returns full string definition for message of type '<VescStateStamped>"
  (cl:format cl:nil "# Timestamped VESC open source motor controller state (telemetry)
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'VescStateStamped)))
  "Returns full string definition for message of type 'VescStateStamped"
  (cl:format cl:nil "# Timestamped VESC open source motor controller state (telemetry)
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <VescStateStamped>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'state))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <VescStateStamped>))
  "Converts a ROS message object to a list"
  (cl:list 'VescStateStamped
    (cl:cons ':header (header msg))
    (cl:cons ':state (state msg))
))