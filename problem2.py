#!/usr/bin/env python

import sys

limit = int(sys.argv[1])
print 'The limit is', limit

def fibonacci():
	a = b = 1
	while True:
		yield a
		a, b = b, a + b

summation = 0
fib = fibonacci()

while True:
	fib_i = fib.next()
	if fib_i > limit:
		break
	if fib_i % 2 == 0:
		summation += fib_i

print 'The result is', summation
