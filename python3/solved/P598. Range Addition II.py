# ToDo:

"""
598. Range Addition II
Easy

Given an m * n matrix M initialized with all 0's and several update operations.

Operations are represented by a 2D array, and each operation is represented by an array with two positive integers a and b, which means M[i][j] should be added by one for all 0 <= i < a and 0 <= j < b.

You need to count and return the number of maximum integers in the matrix after performing all the operations.

Example 1:

Input: 
m = 3, n = 3
operations = [[2,2],[3,3]]
Output: 4
Explanation: 
Initially, M = 
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]

After performing [2,2], M = 
[[1, 1, 0],
 [1, 1, 0],
 [0, 0, 0]]

After performing [3,3], M = 
[[2, 2, 1],
 [2, 2, 1],
 [1, 1, 1]]

So the maximum integer in M is 2, and there are four of it in M. So return 4.

Note:

    The range of m and n is [1,40000].
    The range of a is [1,m], and the range of b is [1,n].
    The range of operations size won't exceed 10,000.


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        
## test part
class Solution:
    def maxCount(self, m, n, ops):
    	"""
    	m: int
    	n: int
    	ops: List[List[int]]
    	rtype: int
    	"""
        
## code here
#1
"""
Success
Runtime: 68 ms, faster than 78.95% of Python3 online submissions for Range Addition II.
Memory Usage: 14.6 MB, less than 33.33% of Python3 online submissions for Range Addition II.
"""
class Solution:
    def maxCount(self, m, n, ops):
        for op in ops:
            i, j = op
            if i < m: m = i
            if j < n: n = j
        return m * n 


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