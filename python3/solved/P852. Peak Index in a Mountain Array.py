# ToDo:

"""
852. Peak Index in a Mountain Array
Easy

Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]

Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Note:
3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
## test part
def peakIndexInMountainArray(A):
	"""
	A: List[int]
	rtype: int
	"""
## code here
#1
"""
Success
Runtime: 80 ms, faster than 60.85% of Python3 online submissions for Peak Index in a Mountain Array.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Peak Index in a Mountain Array.
"""
def peakIndexInMountainArray(A):
	return A.index(max(A))

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_A = [[0,1,0], [0,2,1,0]]
	expected_output = [1, 1]
	for i in range(len(input_A)):
		if peakIndexInMountainArray(input_A[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', peakIndexInMountainArray(input_A[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(peakIndexInMountainArray(input_A[-1]))
	

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