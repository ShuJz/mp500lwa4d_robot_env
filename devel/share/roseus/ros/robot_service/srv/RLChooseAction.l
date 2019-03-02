;; Auto-generated. Do not edit!


(when (boundp 'robot_service::RLChooseAction)
  (if (not (find-package "ROBOT_SERVICE"))
    (make-package "ROBOT_SERVICE"))
  (shadow 'RLChooseAction (find-package "ROBOT_SERVICE")))
(unless (find-package "ROBOT_SERVICE::RLCHOOSEACTION")
  (make-package "ROBOT_SERVICE::RLCHOOSEACTION"))
(unless (find-package "ROBOT_SERVICE::RLCHOOSEACTIONREQUEST")
  (make-package "ROBOT_SERVICE::RLCHOOSEACTIONREQUEST"))
(unless (find-package "ROBOT_SERVICE::RLCHOOSEACTIONRESPONSE")
  (make-package "ROBOT_SERVICE::RLCHOOSEACTIONRESPONSE"))

(in-package "ROS")





(defclass robot_service::RLChooseActionRequest
  :super ros::object
  :slots (_state ))

(defmethod robot_service::RLChooseActionRequest
  (:init
   (&key
    ((:state __state) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _state __state)
   self)
  (:state
   (&optional __state)
   (if __state (setq _state __state)) _state)
  (:serialization-length
   ()
   (+
    ;; float64[] _state
    (* 8    (length _state)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[] _state
     (write-long (length _state) s)
     (dotimes (i (length _state))
       (sys::poke (elt _state i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[] _state
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _state (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _state i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(defclass robot_service::RLChooseActionResponse
  :super ros::object
  :slots (_action ))

(defmethod robot_service::RLChooseActionResponse
  (:init
   (&key
    ((:action __action) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _action __action)
   self)
  (:action
   (&optional __action)
   (if __action (setq _action __action)) _action)
  (:serialization-length
   ()
   (+
    ;; float64[] _action
    (* 8    (length _action)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[] _action
     (write-long (length _action) s)
     (dotimes (i (length _action))
       (sys::poke (elt _action i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[] _action
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _action (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _action i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(defclass robot_service::RLChooseAction
  :super ros::object
  :slots ())

(setf (get robot_service::RLChooseAction :md5sum-) "6904b829fd6bdbea4739bf92ec4b118d")
(setf (get robot_service::RLChooseAction :datatype-) "robot_service/RLChooseAction")
(setf (get robot_service::RLChooseAction :request) robot_service::RLChooseActionRequest)
(setf (get robot_service::RLChooseAction :response) robot_service::RLChooseActionResponse)

(defmethod robot_service::RLChooseActionRequest
  (:response () (instance robot_service::RLChooseActionResponse :init)))

(setf (get robot_service::RLChooseActionRequest :md5sum-) "6904b829fd6bdbea4739bf92ec4b118d")
(setf (get robot_service::RLChooseActionRequest :datatype-) "robot_service/RLChooseActionRequest")
(setf (get robot_service::RLChooseActionRequest :definition-)
      "float64[] state
---
float64[] action
")

(setf (get robot_service::RLChooseActionResponse :md5sum-) "6904b829fd6bdbea4739bf92ec4b118d")
(setf (get robot_service::RLChooseActionResponse :datatype-) "robot_service/RLChooseActionResponse")
(setf (get robot_service::RLChooseActionResponse :definition-)
      "float64[] state
---
float64[] action
")



(provide :robot_service/RLChooseAction "6904b829fd6bdbea4739bf92ec4b118d")


