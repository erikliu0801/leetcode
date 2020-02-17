# ToDo:

"""
976. Largest Perimeter Triangle
Easy

Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.

Note:
3 <= A.length <= 10000
1 <= A[i] <= 10^6

"""
# Conditions & Concepts
"""
Without loss of generality, say the sidelengths of the triangle are a≤b≤c. The necessary and sufficient condition for these lengths to form a triangle of non-zero area is a+b>c.

class Solution(object):
    def largestPerimeter(self, A):
        A.sort()
        for i in xrange(len(A) - 3, -1, -1):
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        return 0
"""
# Code
## submit part
class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        
## test part
def largestPerimeter(A):

## code here
#1
"""
Success
Runtime: 208 ms, faster than 59.65% of Python3 online submissions for Largest Perimeter Triangle.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Largest Perimeter Triangle.
"""
def largestPerimeter(A):
	A.sort(reverse=True)
	for i in range(len(A)-2):
		if A[i] < A[i+1] + A[i+2]:
			return sum(A[i:i+3])
	return 0



# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_A = [[2,1,2], [1,2,1], [3,2,3,4], [3,6,2,3]]
	expected_output = [5, 0, 10, 8]
	for i in range(len(input_A)):
		if largestPerimeter(input_A[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', largestPerimeter(input_A[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(largestPerimeter(input_A[-1]))
	

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