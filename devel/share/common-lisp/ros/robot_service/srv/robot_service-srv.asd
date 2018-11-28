
(cl:in-package :asdf)

(defsystem "robot_service-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "GetModelState" :depends-on ("_package_GetModelState"))
    (:file "_package_GetModelState" :depends-on ("_package"))
  ))