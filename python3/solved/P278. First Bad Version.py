# ToDo:

"""
278. First Bad Version
Easy
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version. 

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
	def firstBadVersion(self, n):
		"""
		:type n: int
		:rtype: int
		"""
		
## test part
def firstBadVersion(n):
## code here
#1
"""
adjust from P69 mySqrt(x)
def mySqrt(x):
	if x < 0: #math.abs(x)
		x = 0 -x
	if x in [0,1]:
		return x
	else:
		try_num = x//2
		high_limit, low_limit = x, 0
		answer = 0
		while answer < 1:
			if try_num**2 > x:
				high_limit = try_num
				if try_num == low_limit +1:
					answer = low_limit
					break
				else:
					try_num = (try_num + low_limit)//2						
			elif try_num**2 < x:
				low_limit = try_num
				if try_num in [high_limit -1, high_limit] :
					answer = try_num
					break
				else:
					try_num = (try_num + high_limit)//2
			else:
				answer = try_num
				break
		return answer

Time Limit Exceeded
2, 1

Wrong Answer
4, 1

Success
Runtime: 28 ms, faster than 75.23% of Python3 online submissions for First Bad Version.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for First Bad Version.
"""
def firstBadVersion(n):
	if n in [0,1] or isBadVersion(n) is False:
		return n
	elif isBadVersion(1) is True:
		return 1
	else:
		try_num = n//2
		high_limit, low_limit = n, 1
		while try_num < n:
			if isBadVersion(try_num) is True:
				high_limit = try_num
				try_num = (high_limit + low_limit) // 2
				if high_limit - 1 == low_limit:
					return high_limit
			elif isBadVersion(try_num) is False:
				low_limit = try_num
				try_num = (high_limit + low_limit) // 2
				if low_limit + 1 == high_limit:
					return high_limit


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