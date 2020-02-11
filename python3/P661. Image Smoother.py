# ToDo:

"""
661. Image Smoother
Easy

Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Note:

    The value in the given matrix is in the range of [0, 255].
    The length and width of the given matrix are in the range of [1, 150].


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        
## test part
def imageSmoother(M):
	"""
	M: List[List[int]]
	rtype: List[List[int]]
	"""
## code here
#1
def imageSmoother(M):
	import numpy as np
	import math #math.floor()
	np_M = np.array(M)
	a, b = np_M.shape
	smothered_M = np.zeros([a,b], dtype = int)
	surrounding = np.ones([a,b])
	for row in np_M:
		surrounding[row+2:] = 0
		for col in row:
			surrounding[col+2:] = 0
			surrounding
			smothered_M[row:col] = np.sum(np_M * surrounding)
		surrounding[row-1] = 0

#1.1
def imageSmoother(M):
	rows = len(M)
	cols = len(M[0])
	smother = []
	for row in rows:
		re_M = M[:row + 2]
		for col in cols:




# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_M = [
	[[1,1,1],
 	[1,0,1],
 	[1,1,1]]]
	expected_output = [
	[[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]]
	for i in range(len(input_M)):
		if imageSmoother(ininput_Mput1[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', imageSmoother(input_M[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(imageSmoother(input_M[-1]))
	

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