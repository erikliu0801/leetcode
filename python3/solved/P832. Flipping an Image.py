# ToDo:

"""
832. Flipping an Image
Easy

Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

1. To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

2. To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

Notes:

    1 <= A.length = A[0].length <= 20
    0 <= A[i][j] <= 1
"""
# Conditions & Concepts
"""
flip then invert
"""
# Code
## submit part
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        
## test part
def flipAndInvertImage(A):
	"""
	A: List[List[int]]
	rtype: List[List[int]]
	"""
## code here
#1
"""
Success
Runtime: 48 ms, faster than 79.31% of Python3 online submissions for Flipping an Image.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Flipping an Image.
"""
def flipAndInvertImage(A):
	for row, arr in enumerate(A):
		for col, element in enumerate(arr.copy()[::-1]):
			if element == 1: A[row][col] = 0 
			else: A[row][col] = 1
	return A

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input1 = [
	[[1,1,0],[1,0,1],[0,0,0]], 
	[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
	]
	expected_output = [
	[[1,0,0],[0,1,0],[1,1,1]], 
	[[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
	]
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