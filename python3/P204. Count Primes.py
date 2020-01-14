# ToDo:

"""
204. Count Primes
Easy
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
	def countPrimes(self, n: int) -> int:
		
## test part
def countPrimes(n):
	"""
	n: int
	rtype: int
	"""
## code here
#1
def countPrimes(n):
	import math
	count = 0
	for i in range(2, int(math.sqrt(n))):
		if n % i == 0:
			count += 1
	return count

#1.1
def countPrimes(n):
	import math
	prime = []
	for i in range(2, int(math.sqrt(n))):
		if n % i == 0:
			prime = prime + [i, n//i]
	return len(set(prime))

#1.2
"""
Input:2
Output:1
Expected:0

Time Limit Exceeded
499979
"""
def countPrimes(n):
	import math
	prime = []
	for m in range(2,n):
		for i in range(2, int(math.sqrt(m))+5):
			if m % i == 0 and m !=i :
				break
			if m % i != 0 and i == int(math.sqrt(m))+4:
				prime.append(m)
	return len(prime)

#1.3
"""
Time Limit Exceeded
499979
"""
def countPrimes(n):
	if n <= 2:
		return 0
	else:
		primes = [2]
		for m in range(2,n):
			for prime in primes:
				if m % prime == 0:
					break
				if m % prime != 0 and prime == primes[-1]:
					primes.append(m)
		return len(primes)

#1.4
"""
Time Limit Exceeded
499979 (41537)
"""
def countPrimes(n):
	if n <= 2:
		return 0
	else:
		primes = [2]
		for m in range(2,n):
			if m % 2 == 0:
				continue
			for prime in primes:
				if m % prime == 0:
					break
				if m % prime != 0 and (prime == primes[-1] or prime**2 > m):
					primes.append(m)
					break
		return len(primes)

#1.5
"""
Time Limit Exceeded
999983 (78497)
"""
def countPrimes(n):
	if n <= 2:
		return 0
	elif n<=10:
		primes = [2]
		for m in range(2,n):
			for prime in primes:
				if m % prime == 0:
					break
				if m % prime != 0 and (prime == primes[-1] or prime**2 > m):
					primes.append(m)
					break
		return len(primes)
	else:
		primes_under_ten = [2,3,5,7]
		primes = [11]
		for m in range(10,n): #
			if m %2 == 0 or m %3 == 0 or m %5 == 0 or m %7 == 0:
				continue
			for prime in primes:
				if m % prime == 0:
					break
				if m % prime != 0 and (prime == primes[-1] or prime**2 > m):
					primes.append(m)
					break
		return len(primes+primes_under_ten)

#1.6
def countPrimes(n):
	if n <= 2:
		return 0
	else:
		primes = [2]
		for m in range(2,n):
			if m % prime in primes == 0:
				continue
			else:
				primes.append(m)
		return len(primes)

#2
"""
Sieve of Eratosthenes
Time Limit Exceeded
input: 10000 (0.36s)
input: 100000 (33s)
"""
def countPrimes(n):
	import time
	now = time.time()
	if n <= 2:
		return 0
	else:
		primes = [2]
		x = set(range(2,n,2))
		for m in list(range(3,n,2)):
			if m in x:
				continue
			else:
				primes.append(m)
				x = x | set(range(m,n,m))
		print(time.time() - now)
		return len(primes)

#2.1
"""
type(primes): list => set
input: 10000 (0.24s)
input: 100000 (25s)
input: 1000000 (s)

Time Limit Exceeded
"""
def countPrimes(n):
	import time 
	now = time.time() 
	if n <= 2:
		return 0
	else:
		primes = set({2}) ##
		x = set(range(2,n,2))
		for m in range(3,n):
			if m in x:
				continue
			else:
				primes.add(m)
				x = x | set(range(m,n,m))
		print(time.time() - now)
		return len(primes)

#2.2
"""
input: 10000 (0.25s)
input: 100000 (24.91s)
input: 1000000 (s)
"""
def countPrimes(n):
	import time
	now = time.time()
	if n <= 2:
		return 0
	else:
		primes = set({2}) ##
		x = set(range(2,n,2))
		for m in list(range(3,n,2)): ##list
			if m in x:
				continue
			else:
				primes.add(m)
				x = x | set(range(m,n,m))
		print(time.time() - now)
		return len(primes)

#2.3
"""
input: 10000 (0.43s)
input: 100000 (25.01s)
input: 1000000 (s)
"""
def countPrimes(n):
	import time
	now = time.time()
	if n <= 2:
		return 0
	else:
		primes = set({2}) ##
		x = set(range(2,n,2))
		for m in tuple(range(3,n,2)): ##tuple
			if m in x:
				continue
			else:
				primes.add(m)
				x = x | set(range(m,n,m))
		print(time.time() - now)
		return len(primes)

# 3
"""
set(x) - set(prime)

input: 10000 (0.45s)
input: 100000 (5.99s)
input: 1000000 (s)

Time Limit Exceeded
"""
def countPrimes(n):
	import time
	now = time.time()
	if n <= 2:
		return 0
	else:
		primes = set({2}) 
		x = set(range(2,n)) - set(range(2,n,2))
		while len(x) != 0:
			prime = min(x)
			primes.add(prime)
			x -= set(range(prime,n,prime))
		print(time.time() - now)
		return len(primes)

#3.1 X
"""
input: 10000 (0.38s) V
input: 100000 (16.64s) X
"""
def countPrimes(n):
	import time
	now = time.time()
	if n <= 2:
		return 0
	else:
		primes = set({2}) 
		x = set(range(2,n)) - set(range(2,n,2))
		while len(x) != 0:
			primes.add(min(x)) #
			x -= set(range(min(x),n,min(x))) #
		print(time.time() - now)
		return len(primes)

#3.2
"""
input: 10000 (0.65s) X
input: 100000 (4.96s) V
"""
def countPrimes(n):
	import time
	now = time.time()
	if n <= 2:
		return 0
	else:
		primes = set({2}) 
		x = set(range(3,n,2)) #
		while len(x) != 0:
			prime = min(x)
			primes.add(prime)
			x -= set(range(prime,n,prime))
		print(time.time() - now)
		return len(primes)

#3.3
"""
input: 10000 (0.06s) VV
input: 100000 (4.02s) V

"""
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
			x -= x & set(range(prime,n,prime)) #
		print(time.time() - now)
		return len(primes)

#3.4
"""
input: 10000 (0.18s) X
input: 100000 (4.74s) X
"""
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
			x.difference_update(set(range(prime,n,prime))) #
		print(time.time() - now)
		return len(primes)

#3.5
"""
input: 10000 (0.10s) V
input: 100000 (4.61s) V
input: 100000 (242.53s) V
"""
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
			primes.add(prime) #
			x -= x.intersection(set(range(prime,n,prime))) #
		print(time.time() - now)
		return len(primes)

#4
"""
input: 10000 (0.005s) VV
input: 100000 (0.42s) VV
input: 100000 (1.73s) VV

Success
Runtime: 2428 ms, faster than 5.02% of Python3 online submissions for Count Primes.
Memory Usage: 124.6 MB, less than 20.69% of Python3 online submissions for Count Primes.
"""
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