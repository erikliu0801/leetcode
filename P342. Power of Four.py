# ToDo:

"""
342. Power of Four
Easy
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:

Input: 16
Output: true
Example 2:

Input: 5
Output: false
Follow up: Could you solve it without loops/recursion?

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        
## test part
def isPowerOfFour(num):
	"""
	num: int
	rtype: bool
	"""
## code here
#1
"""
Input: 2
Output: true
Expected: false
"""
# def isPowerOfFour(num):
# 	if num <= 0:
# 		return False
# 	import math
# 	max_int = 2**31-1
# 	max_power = int(math.log(max_int,4))
# 	return 4**max_power % num == 0

#1.1
"""
ajust from P231 isPowerOfTwo(n)
def isPowerOfTwo(n):
	if n%2 == 1 and n != 1:
		return False
	else:
		i = 0
		while 2**i <= n:
			if 2**i == n:
				return True
			i += 1
		return False

Success
Runtime: 24 ms, faster than 95.30% of Python3 online submissions for Power of Four.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Power of Four.
"""
def isPowerOfFour(num):
	if num <= 0:
		return False
	elif num%2 == 1 and num != 1:
		return False
	else:
		i = 0
		while 4**i <= num:
			if 4**i == num:
				return True
			i += 1
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