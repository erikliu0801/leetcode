# ToDo:

"""
70. Climbing Stairs
Easy

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def climbStairs(self, n: int) -> int:
## test part
def climbStairs(n):
	"""
	n: int
	rtype: int
	"""
## code here
#1
def climbStairs(n):

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_int = [2, 3]
	expected_output = [2, 3]
	for i in range(len(input_int)):
		if climbStairs(input_int[i]) != expected_output[i]:
			print("Wrong!!!")
			print(climbStairs(input_int[i]))
		else:
			print("Right")		
	# print(climbStairs(input_int[-1]))
	

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