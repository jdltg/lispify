;; Load Hunchentoot using Quicklisp
(ql:quickload :hunchentoot)

;; Define a package that exports the start and stop functions
(defpackage :lisp-server
  (:use :cl :hunchentoot)
  (:export :start-server :stop-server))

(in-package :lisp-server)

;; Define a handler for the /execute endpoint
(define-easy-handler (execute-lisp :uri "/execute") (code)
  (let ((result (ignore-errors
                  (let ((*package* (find-package :cl))) ; Evaluate in CL package
                    (eval (read-from-string code))))))
    (setf (hunchentoot:content-type*) "text/plain")
    (format nil "~A" (or result "Error"))))

;; Global server variable
(defvar *server* nil)

;; Start server on specified port
(defun start-server (&optional (port 8080))
  (setf *server* (make-instance 'easy-acceptor :port port))
  (start *server*)
  (format t "Lisp server started at http://localhost:~A~%" port))

;; Stop the server
(defun stop-server ()
  (when *server*
    (stop *server*)
    (setf *server* nil)
    (format t "Server stopped.~%")))
