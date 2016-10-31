#! /usr/bin/env python
for ii in range(1, 101):
    msg = ''
    if ii % 3 == 0:
        msg += 'Fizz'
    if ii % 5 == 0:
        msg += 'Buzz'
    print(msg or ii)
