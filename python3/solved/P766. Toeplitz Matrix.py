# ToDo:

"""
766. Toeplitz Matrix
Easy

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

Note:

    matrix will be a 2D array of integers.
    matrix will have a number of rows and columns in range [1, 20].
    matrix[i][j] will be integers in range [0, 99].

Follow up:

    What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
    What if the matrix is so large that you can only load up a partial row into the memory at once?

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
## test part
def isToeplitzMatrix(matrix):
	"""
	matrix: List[List[int]]
	rtype: bool
	"""
## code here
#1
"""
Success
Runtime: 88 ms, faster than 66.64% of Python3 online submissions for Toeplitz Matrix.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Toeplitz Matrix.
"""
def isToeplitzMatrix(matrix):
	array = []
	for i, arr in enumerate(matrix):
		if i == 0:
			array = arr
			continue
		for j, val in enumerate(arr):
			if j == 0:
				array.insert(0,val)
				continue
			if array[j] != val: return False
	return True



# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_matrix = [
	[[1,2,3,4],
	 [5,1,2,3],
	 [9,5,1,2]],
	[[1,2],
	 [2,2]]]
	expected_output = [True, False]
	for i in range(len(input_matrix)):
		if isToeplitzMatrix(input_matrix[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', isToeplitzMatrix(input_matrix[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(isToeplitzMatrix(input_matrix[-1]))
	

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