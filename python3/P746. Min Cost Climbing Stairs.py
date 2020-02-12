# ToDo:

"""
746. Min Cost Climbing Stairs
Easy

On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
## test part
def minCostClimbingStairs(cost):
	"""
	cost: List[int]
	rtype: int
	"""
## code here
#1
def minCostClimbingStairs(cost):


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input1 = [[10, 15, 20], [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]]
	expected_output = [15, 6]
	for i in range(len(input1)):
		if func(input1[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', func(input1[i]), '; Expected Output:', expected_output[i])
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