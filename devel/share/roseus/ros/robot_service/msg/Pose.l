;; Auto-generated. Do not edit!


(when (boundp 'robot_service::Pose)
  (if (not (find-package "ROBOT_SERVICE"))
    (make-package "ROBOT_SERVICE"))
  (shadow 'Pose (find-package "ROBOT_SERVICE")))
(unless (find-package "ROBOT_SERVICE::POSE")
  (make-package "ROBOT_SERVICE::POSE"))

(in-package "ROS")
;;//! \htmlinclude Pose.msg.html


(defclass robot_service::Pose
  :super ros::object
  :slots (_position _orientation ))

(defmethod robot_service::Pose
  (:init
   (&key
    ((:position __position) (instance robot_service::Point :init))
    ((:orientation __orientation) (instance robot_service::Quaternion :init))
    )
   (send-super :init)
   (setq _position __position)
   (setq _orientation __orientation)
   self)
  (:position
   (&rest __position)
   (if (keywordp (car __position))
       (send* _position __position)
     (progn
       (if __position (setq _position (car __position)))
       _position)))
  (:orientation
   (&rest __orientation)
   (if (keywordp (car __orientation))
       (send* _orientation __orientation)
     (progn
       (if __orientation (setq _orientation (car __orientation)))
       _orientation)))
  (:serialization-length
   ()
   (+
    ;; robot_service/Point _position
    (send _position :serialization-length)
    ;; robot_service/Quaternion _orientation
    (send _orientation :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; robot_service/Point _position
       (send _position :serialize s)
     ;; robot_service/Quaternion _orientation
       (send _orientation :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; robot_service/Point _position
     (send _position :deserialize buf ptr-) (incf ptr- (send _position :serialization-length))
   ;; robot_service/Quaternion _orientation
     (send _orientation :deserialize buf ptr-) (incf ptr- (send _orientation :serialization-length))
   ;;
   self)
  )

(setf (get robot_service::Pose :md5sum-) "e45d45a5a1ce597b249e23fb30fc871f")
(setf (get robot_service::Pose :datatype-) "robot_service/Pose")
(setf (get robot_service::Pose :definition-)
      "# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: robot_service/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: robot_service/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

")



(provide :robot_service/Pose "e45d45a5a1ce597b249e23fb30fc871f")


