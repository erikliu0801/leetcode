# ToDo:

"""
263. Ugly Number
Easy
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example 1:

Input: 6
Output: true
Explanation: 6 = 2 × 3
Example 2:

Input: 8
Output: true
Explanation: 8 = 2 × 2 × 2
Example 3:

Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.
Note:

1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−2**31,  2**31 − 1].

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def isUgly(self, num: int) -> bool:
        
## test part
def isUgly(num):
	"""
	num: int
	rtype: bool
	"""
## code here
#1
"""
adjust from P204
def countPrimes(n):
	import time
	now = time.time()
	if n <= 2:
		return 0
	else:
		primes = set({2})
		x = set(range(3,n,2))
		while len(x) != 0:
			prime = min(x)
			primes.add(prime)
			x.remove(prime)
			x -= x.intersection(set(range(prime**2,n,prime))) 
			##
			if prime**2 >= n: 
				break
		primes |= x
		print(time.time() - now)
		return len(primes)
"""
# def findPrimes(num):
# 	"""
# 	n : int
# 	rtype: set
# 	"""
# 	import math
# 	n = int(math.sqrt(num))
# 	if n == 1:
# 		return set()
# 	elif n < 2:
# 		return set([num])
# 	else:
# 		primes = set({2})
# 		x = set(range(3,n,2))
# 		while len(x) != 0:
# 			prime = min(x)
# 			primes.add(prime)
# 			x.remove(prime)
# 			x -= x.intersection(set(range(prime**2,n,prime))) 
# 			##
# 			if prime**2 >= n: 
# 				break
# 		primes |= x
# 	for posible_prime in primes.copy():
# 		if num % posible_prime != 0:
# 			primes.remove(posible_prime)
# 	##
# 	return primes


#1.1
def primeFactorization(num):
	prime = 2
	checked_primes = [2]
	primes = []
	while prime < num:
		if num % prime == 0:
			primes.append(prime)
			while num // prime != 0:
				num = num // prime
		else:
			while prime < num:
				prime += 1
				for checked_prime in checked_primes:
					if prime % checked_prime == 0:
						break
				checked_primes.append(prime)
		return primes

#1.2
"""
Memory Limit Exceeded
Last executed input: 214797179
"""
	def primeFactorization(num):
		prime = 2
		checked_primes = set({2})
		x = set(range(3,num+1,2))
		primes = set()
		while prime <= num:
			if num % prime == 0:
				primes.add(prime)
				while num % prime == 0:
					num = num // prime
			if len(x) != 0:
				prime = min(x)
				checked_primes.add(prime)
				x.remove(prime)
				x -= x.intersection(set(range(prime**2,num+1,prime)))
		return primes


def isUgly(num):
	def primeFactorization(num):
		prime = 2
		checked_primes = set({2})
		x = set(range(3,num+1,2))
		primes = set()
		while prime <= num:
			if num % prime == 0:
				primes.add(prime)
				while num % prime == 0:
					num = num // prime
			if len(x) != 0:
				prime = min(x)
				checked_primes.add(prime)
				x.remove(prime)
				x -= x.intersection(set(range(prime**2,num+1,prime)))
		return primes
	if num <= 0:
		return False
	num_primes = primeFactorization(num)
	if num_primes - set({2,3,5}) == set({}):
		return True
	return False

#1.3
"""
Success
Runtime: 28 ms, faster than 87.99% of Python3 online submissions for Ugly Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Ugly Number.
"""
def isUgly(num):
	if num <= 0:
		return False
	ugly_num_primes = [2,3,5]
	for ugly_num_prime in ugly_num_primes:
		while num % ugly_num_prime == 0:
			num = num // ugly_num_prime
	if num == 1:
		return True
	return False


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input1 = []
	expected_output = []
	for i in range(len(input1)):
		if func(input1[i]) != expected_output[i]:
			print("Wrong!!!")
			print(func(input1[i]))
		else:
			print("Right")		
	# print(func(input1[-1]))
	

## Performance Test
import cProfile
cProfile.run('')


## Unit Test
import unittest
class Test(unittest.TestCase):
	def test(self):
		pass

if __name__ == '__main__':
    unittest.main()