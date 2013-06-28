#!/usr/bin/env python

def sum_of_n(n):
	return n * (n + 1) / 2

def sum_of_multiples(limit = 1000, prime1 = 3, prime2 = 5):
	multiples_for_prime1 = limit / prime1
	multiples_for_prime2 = limit / prime2
	return prime1 * sum_of_n(multiples_for_prime1) + prime2 * sum_of_n(multiples_for_prime2)

print sum_of_multiples()
