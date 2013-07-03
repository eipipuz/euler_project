#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import problem3

def get_max_palindrome(n_digits):
	"""
	The maximum product a number with N digits can have is:
	max_int = int('9' * n_digits) # For example 99
	max_multiplication = max_int ** 2 # e.g. 99 * 99

	If you check several products you see a pattern, these numbers are 81, 9801, 998001, etc. Hence the maximum palindrome for them is 77, 9779, 997799, etc.
	"""
	max_palindrome = ('9'*(n_digits-1)) + '77' + ('9'*(n_digits-1))
	return int(max_palindrome)

def number_of_digits(n):
	"""
	Log base 10 is the cheapest way to calculate it. «len(str(n))» doesn't perform as well. The downside is that it doesn't handle well non-positive numbers. Not a problem for now.
	"""
	if n == 0:
		return 1
	size = math.log10(n) + 1
	return int(size)

def get_root(palindrome):
	"""
	The root of a palindrome is the part of the number that is unique.
	For example: 12344321 -> 1234, 23432 -> 234
	"""
	str_palindrome = str(palindrome)
	length_palindrome = len(str_palindrome)
	middle_position =  int(math.ceil(length_palindrome / 2.0))
	str_root = str_palindrome[:middle_position]
	return int(str_root)

def number_of_palindromes_with_N_digits(n):
	"""
	#    -> 10
	##   -> 9 + 10 = 19
	###  -> 9*10 + 19 = 109
	#### -> 9*100 + 109 = 1009

	We don't use the recursive function because we can do it in linear time.

		return 9*(10**(n-2)) + number_of_palindromes_with_N_digits(n-1)
	"""
	if n == 1:
		return 10
	else:
		return 9 + 10**(n-1)

def palindrome_desc_list(n):
	"""
	So if we get 77, we should return [77, 66, 55, ...]
	So if we get 9779, we should return [9779, 9669, ..., 9009, 8998,
	..., 1001, 999, 989, ...]

	We will work with a list, so we want a generator
	"""
	root = get_root(n)
	palindrome_size = number_of_digits(n)
	root_size = number_of_digits(root)
	while True:
		if palindrome_size == 2 and root == 0: # if '00' then become '9'
			root = 9
			palindrome_size = 1
			root_size = 1
			str_palindrome = '9'
		elif palindrome_size % 2 == 0: # then mirror it
			str_palindrome = str(root) + str(root)[::-1]
		elif root == 0:
			raise StopIteration
		else: # mirror but skip the last digit
			str_palindrome = str(root) + str(root)[:-1][::-1]
		yield int(str_palindrome)
		root -= 1
		if root_size > number_of_digits(root):
			next_palindrome = '9' * (palindrome_size - 1)
			root = get_root(int(next_palindrome))
			palindrome_size -= 1
			root_size = number_of_digits(root)

def ways_to_split_in_two_a_set(set_of_primes):
	"""
	{a,b} can only be split into {a,b}. So f(2) = 1
	{a,b,c} can be split into {a,{b,c}}, {b,{a,c}} & {c,{a,b}}. So f(3) = 3
	The pattern is roughly, you have 3 families:
	* the solution of f(n-1) adding the extra element to the left
	* the solution of f(n-1) adding the extra element to the right
	* the extra element on one side and all the others in the other side.

	Therefore f(n) = 2f(n-1) + 1; f(n) = 2**(n-1) - 1
	"""
	if len(set_of_primes) == 2:
		ways = [([set_of_primes[0]], [set_of_primes[1]])]
	else:
		simpler_ways = ways_to_split_in_two_a_set(set_of_primes[:-1])
		import copy
		side_left = copy.deepcopy(simpler_ways)
		del copy
		for way in side_left:
			(way_left, way_right) = way
			way_right.append(set_of_primes[-1])
		ways = side_left
		side_right = simpler_ways
		for way in side_right:
			(way_left, way_right) = way
			way_left.append(set_of_primes[-1])
		ways += side_right
		ways.append(([set_of_primes[-1]], set_of_primes[:-1])) 
	return ways

def found_possible_combination(factors):
	for (side_a, side_b)  in ways_to_split_in_two_a_set(factors):
		mult = lambda x, y: x*y
		factor_a = reduce(mult, side_a)
		if number_of_digits(factor_a) != 2:
			continue
		factor_b = reduce(mult, side_b)
		if number_of_digits(factor_b) == 2:
			return (factor_a, factor_b)
	return None

def find_max_palindrome_product_of_numbers_with_N_digits(n):
	"""
	We first get the maximum palindrome that it could be, then we get a list in descending order. Each palindrome is tested in several ways until we find one that we like.
	"""
	max_palindrome = get_max_palindrome(n)
	palindromes = palindrome_desc_list(max_palindrome)
	for p in palindromes:
		factors = problem3.factorize(p)
		if len(factors) == 1: #it's a prime
			continue
		if number_of_digits(factors[-1]) > n:
			continue
		if len(factors) == 2 and number_of_digits(factors[0]) == n and number_of_digits(factors[1]) == n:
			return tuple(factors)
		#print p, factors
		combination = found_possible_combination(factors)
		if combination:
			return combination
