# ToDo:

"""
1351. Count Negative Numbers in a Sorted Matrix
Easy

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 

Return the number of negative numbers in grid.

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
## test part
def countNegatives(grid):
	"""
	grid: List[List[int]]
	rtpye: int
	"""
## code here
#1
"""
Success
Runtime: 116 ms, faster than 98.65% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
"""
def countNegatives(grid):
	count = 0
	row = len(grid[0])
	for col in grid:
		for i, e in enumerate(col):
			if e < 0: 
				count += row-i
				break
	return count

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_grid = [
		[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]], 
		[[3,2],[1,0]],
		[[1,-1],[-1,-1]],
		[[-1]]
	]
	expected_output = [8, 0, 3, 1]
	for i in range(len(input_grid)):
		if countNegatives(input_grid[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', countNegatives(input_grid[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(countNegatives(input_grid[-1]))
	

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