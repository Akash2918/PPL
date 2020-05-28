(defun factorial (n)
  (if ( = n 0)
    1
    ( * n (factorial ( - n 1)))))

(print "Enter the number : ")
(setq n (read))
(factorial n)
(print "The value of the factorial is : ")
(print n)
