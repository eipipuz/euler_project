#!/usr/bin/env python

import math
def factorize(n, factors = None):
	if factors is None:
		factors = []
	
	max_factor = int(math.floor(math.sqrt(n))) + 1
	for i in xrange(2, max_factor):
		if n % i == 0:
			factors.append(i)
			n /= i
			return factorize(n, factors)
	factors.append(n)
	return factors

if __name__ == "__main__":
	import sys
	n = int(sys.argv[1])
	if not n:
		exit(1)


	factors = factorize(n)
	print 'The largest prime factor of the number', n, 'is', factors[-1]
