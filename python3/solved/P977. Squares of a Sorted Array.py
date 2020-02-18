# ToDo:

"""
977. Squares of a Sorted Array
Easy

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Note:
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        
## test part
def sortedSquares(A):
	"""
	A: List[int]
	rtype: List[int]
	"""

## code here
#1
"""
Success
Runtime: 232 ms, faster than 78.69% of Python3 online submissions for Squares of a Sorted Array.
Memory Usage: 14.7 MB, less than 95.24% of Python3 online submissions for Squares of a Sorted Array.
"""
def sortedSquares(A):
	A = [x**2 for x in A]
	A.sort()
	return A

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_A = [[-4,-1,0,3,10], [-7,-3,2,3,11]]
	expected_output = [[0,1,9,16,100], [4,9,9,49,121]]
	for i in range(len(input_A)):
		if sortedSquares(input_A[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', sortedSquares(input_A[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(sortedSquares(input_A[-1]))
	

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