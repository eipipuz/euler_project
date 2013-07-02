#!/usr/bin/env python

import unittest
import problem4

class TestProblem4(unittest.TestCase):
	def setUp(self):
		pass

	def test_number_of_digits(self):
		size = problem4.number_of_digits(1)
		self.assertEqual(size, 1)
		size = problem4.number_of_digits(12344321)
		self.assertEqual(size, 8)
		size = problem4.number_of_digits(23432)
		self.assertEqual(size, 5)

	def test_get_root(self):
		root = problem4.get_root(1)
		self.assertEqual(root, 1)
		root = problem4.get_root(12344321)
		self.assertEqual(root, 1234)
		root = problem4.get_root(23432)
		self.assertEqual(root, 234)
		pass

	def test_number_of_palindromes_with_N_digits(self):
		n = problem4.number_of_palindromes_with_N_digits(1)
		self.assertEqual(n, 10)
		n = problem4.number_of_palindromes_with_N_digits(3)
		self.assertEqual(n, 109)
		n = problem4.number_of_palindromes_with_N_digits(4)
		self.assertEqual(n, 1009)

if __name__ == '__main__':
	unittest.main()
