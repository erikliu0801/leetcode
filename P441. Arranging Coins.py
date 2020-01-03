# ToDo:

"""
441. Arranging Coins
Easy

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.

Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def arrangeCoins(self, n: int) -> int:
        
## test part
def arrangeCoins(n):
	"""
	n: int
	rtype: int
	"""
## code here
#1
"""
Wrong Answer
Input:2
Output:2
Expected:1

Success
Runtime: 1124 ms, faster than 22.67% of Python3 online submissions for Arranging Coins.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Arranging Coins.
"""
def stairCase(n):
	if n == 1:
		return n
	else:
		return n + stairCase(n-1)

def arrangeCoins(n):
	stair = 1
	staircase = 1
	staircase_sum = 1
	while staircase_sum <= n:
		stair += 1
		staircase += 1		
		staircase_sum += staircase
	if staircase_sum == n:
		return stair
	return stair-1



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