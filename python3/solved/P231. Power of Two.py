# ToDo:

"""
231. Power of Two
Easy
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 2**0 = 1
Example 2:

Input: 16
Output: true
Explanation: 2**4 = 16
Example 3:

Input: 2**18
Output: false

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
## test part
def isPowerOfTwo(n):
	"""
	n: int
	rtype: bool
	"""
## code here
#1
"""
Success
Runtime: 32 ms, faster than 63.85% of Python3 online submissions for Power of Two.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Power of Two.
"""
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