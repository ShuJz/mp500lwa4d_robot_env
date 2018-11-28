;; Auto-generated. Do not edit!


(when (boundp 'robot_service::Twist)
  (if (not (find-package "ROBOT_SERVICE"))
    (make-package "ROBOT_SERVICE"))
  (shadow 'Twist (find-package "ROBOT_SERVICE")))
(unless (find-package "ROBOT_SERVICE::TWIST")
  (make-package "ROBOT_SERVICE::TWIST"))

(in-package "ROS")
;;//! \htmlinclude Twist.msg.html


(defclass robot_service::Twist
  :super ros::object
  :slots (_linear _angular ))

(defmethod robot_service::Twist
  (:init
   (&key
    ((:linear __linear) (instance robot_service::Vector3 :init))
    ((:angular __angular) (instance robot_service::Vector3 :init))
    )
   (send-super :init)
   (setq _linear __linear)
   (setq _angular __angular)
   self)
  (:linear
   (&rest __linear)
   (if (keywordp (car __linear))
       (send* _linear __linear)
     (progn
       (if __linear (setq _linear (car __linear)))
       _linear)))
  (:angular
   (&rest __angular)
   (if (keywordp (car __angular))
       (send* _angular __angular)
     (progn
       (if __angular (setq _angular (car __angular)))
       _angular)))
  (:serialization-length
   ()
   (+
    ;; robot_service/Vector3 _linear
    (send _linear :serialization-length)
    ;; robot_service/Vector3 _angular
    (send _angular :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; robot_service/Vector3 _linear
       (send _linear :serialize s)
     ;; robot_service/Vector3 _angular
       (send _angular :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; robot_service/Vector3 _linear
     (send _linear :deserialize buf ptr-) (incf ptr- (send _linear :serialization-length))
   ;; robot_service/Vector3 _angular
     (send _angular :deserialize buf ptr-) (incf ptr- (send _angular :serialization-length))
   ;;
   self)
  )

(setf (get robot_service::Twist :md5sum-) "9f195f881246fdfa2798d1d3eebca84a")
(setf (get robot_service::Twist :datatype-) "robot_service/Twist")
(setf (get robot_service::Twist :definition-)
      "# This expresses velocity in free space broken into its linear and angular parts.
Vector3  linear
Vector3 angular

================================================================================
MSG: robot_service/Vector3
float64 x
float64 y
float64 z

")



(provide :robot_service/Twist "9f195f881246fdfa2798d1d3eebca84a")


