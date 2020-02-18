# ToDo:

"""
1337. The K Weakest Rows in a Matrix
Easy

Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is, always ones may appear first and then zeros. 

Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 2 
row 1 -> 4 
row 2 -> 1 
row 3 -> 2 
row 4 -> 5 
Rows ordered from the weakest to the strongest are [2,0,3,1,4]

Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 1 
row 1 -> 4 
row 2 -> 1 
row 3 -> 1 
Rows ordered from the weakest to the strongest are [0,2,3,1]

Constraints:
m == mat.length
n == mat[i].length
2 <= n, m <= 100
1 <= k <= m
matrix[i][j] is either 0 or 1.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
## test part
def kWeakestRows(mat, k):
	"""
	mat: List[List[int]]
	k: int
	rtype: List[int]
	"""
## code here
#1
"""
Success
Runtime: 112 ms, faster than 76.61% of Python3 online submissions for The K Weakest Rows in a Matrix.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for The K Weakest Rows in a Matrix.
"""
def kWeakestRows(mat, k):
	row_nums = []
	for row in mat:
		row_nums.append(sum(row))
	row_nums_sort = row_nums.copy()
	row_nums_sort.sort()
	del mat, row
	for i, num in enumerate(row_nums_sort):
		j = row_nums.index(num)
		row_nums_sort[i] = j
		#row_nums[j] = True #####!!!!????
		row_nums[j] = -1
	del i, j, num, row_nums, row_nums_sort[k:]
	return row_nums_sort


# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_mat = [[[1, 1, 0, 0, 0],
				  [1, 1, 1, 1, 0],
				  [1, 0, 0, 0, 0],
				  [1, 1, 0, 0, 0],
				  [1, 1, 1, 1, 1]],
				 [[1, 0, 0, 0],
				  [1, 1, 1, 1],
				  [1, 0, 0, 0],
				  [1, 0, 0, 0]]
				 ]
	input_k = [3, 2]
	expected_output = [[2, 0, 3], [0, 2]]
	for i in range(len(input_mat)):
		if kWeakestRows(input_mat[i], input_k[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', kWeakestRows(input_mat[i], input_k[i]), '; Expected Output:',
				  expected_output[i])
		else:
			print("Right")
# print(kWeakestRows(input_mat[-1], input_k[-1]))
	

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