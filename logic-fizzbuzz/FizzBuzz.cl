(loop for ii from 1 to 100 do
     (cond
       ((zerop (mod ii 15)) (print "FizzBuzz"))
       ((zerop (mod ii 3)) (print "Fizz"))
       ((zerop (mod ii 5)) (print "Buzz"))
       ((zerop 0) (print ii))
       ))
