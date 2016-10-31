cdef int ii = 0
for ii in range(1, 101):
    if ii % 15 == 0:
        print("FizzBuzz")
    elif ii % 3 == 0:
        print("Fizz")
    elif ii % 5 == 0:
        print("Buzz")
    else:
        print(ii)
