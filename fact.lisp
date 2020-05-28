(print "Enter the number : ")
(setq n (read))
(setq result 1)

(defun fact(n)
  ( loop for x from 1 to n
	do (setq result (* result x))
	)
  )
(fact n)
(print "The Factorial of given number is :")
(print result)
