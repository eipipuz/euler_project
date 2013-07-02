#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import problem3

def max_palindrome(n_digits):
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

def palindrome_desc_list(max_palindrome):
	"""
	So if we get 77, we should return [77, 66, 55, ...]
	So if we get 9779, we should return [9779, 9669, ..., 9009, 8998,
	..., 1001, 999, 989, ...]

	We will work with a list, so we want a generator
	"""
	current_root = get_root(max_palindrome)
	palindrome_size = number_of_digits(max_palindrome)
	size = number_of_digits(current_root)
	while True:
		if current_root == 0:
			if palindrome_size == 1:
				raise StopIteration
			else:
				current_root = 9
				palindrome_size = 1
				size = 1
		if palindrome_size % 2 == 0:
			str_root = str(current_root) + str(current_root)[::-1]
		else:
			str_root = str(current_root) + str(current_root)[:-1][::-1]
		yield int(str_root)
		current_root -= 1
		if size > number_of_digits(current_root):
			next_palindrome = '9' * (palindrome_size - 1)
			current_root = get_root(int(next_palindrome))
			palindrome_size -= 1
			size = number_of_digits(current_root)
