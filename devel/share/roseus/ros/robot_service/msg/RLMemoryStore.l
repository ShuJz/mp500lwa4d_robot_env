;; Auto-generated. Do not edit!


(when (boundp 'robot_service::RLMemoryStore)
  (if (not (find-package "ROBOT_SERVICE"))
    (make-package "ROBOT_SERVICE"))
  (shadow 'RLMemoryStore (find-package "ROBOT_SERVICE")))
(unless (find-package "ROBOT_SERVICE::RLMEMORYSTORE")
  (make-package "ROBOT_SERVICE::RLMEMORYSTORE"))

(in-package "ROS")
;;//! \htmlinclude RLMemoryStore.msg.html


(defclass robot_service::RLMemoryStore
  :super ros::object
  :slots (_s _a _r _s_ ))

(defmethod robot_service::RLMemoryStore
  (:init
   (&key
    ((:s __s) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:a __a) (make-array 0 :initial-element 0.0 :element-type :float))
    ((:r __r) 0.0)
    ((:s_ __s_) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _s __s)
   (setq _a __a)
   (setq _r (float __r))
   (setq _s_ __s_)
   self)
  (:s
   (&optional __s)
   (if __s (setq _s __s)) _s)
  (:a
   (&optional __a)
   (if __a (setq _a __a)) _a)
  (:r
   (&optional __r)
   (if __r (setq _r __r)) _r)
  (:s_
   (&optional __s_)
   (if __s_ (setq _s_ __s_)) _s_)
  (:serialization-length
   ()
   (+
    ;; float64[] _s
    (* 8    (length _s)) 4
    ;; float64[] _a
    (* 8    (length _a)) 4
    ;; float64 _r
    8
    ;; float64[] _s_
    (* 8    (length _s_)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[] _s
     (write-long (length _s) s)
     (dotimes (i (length _s))
       (sys::poke (elt _s i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64[] _a
     (write-long (length _a) s)
     (dotimes (i (length _a))
       (sys::poke (elt _a i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;; float64 _r
       (sys::poke _r (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64[] _s_
     (write-long (length _s_) s)
     (dotimes (i (length _s_))
       (sys::poke (elt _s_ i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[] _s
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _s (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _s i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64[] _a
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _a (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _a i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;; float64 _r
     (setq _r (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64[] _s_
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _s_ (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _s_ i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get robot_service::RLMemoryStore :md5sum-) "ee95e3c395c129a7450df7cde8e1479b")
(setf (get robot_service::RLMemoryStore :datatype-) "robot_service/RLMemoryStore")
(setf (get robot_service::RLMemoryStore :definition-)
      "float64[] s
float64[] a
float64 r
float64[] s_
")



(provide :robot_service/RLMemoryStore "ee95e3c395c129a7450df7cde8e1479b")


