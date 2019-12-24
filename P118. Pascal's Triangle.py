# ToDo:

"""
118. Pascal's Triangle
Easy

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
## test part
def generate(numRows):
	"""
	numRows: int
	rtype: List[List[int]]
	"""
## code here
#1
"""
Success
Runtime: 24 ms, faster than 94.56% of Python3 online submissions for Pascal's Triangle.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle.
"""
def generate(numRows):
	def levelOfPascal(num):
		if num == 1:
			return [1]
		elif num ==2:
			return [1,1]
		else:
			pre_level = levelOfPascal(num-1)
			for i in range(len(pre_level)-1):
				pre_level[i] = pre_level[i] + pre_level[i+1]
			level = [1] + pre_level
			return level
	if numRows == 0:
		return 
	else:
		Triangle = []
		for i in range(1,numRows+1):
			Triangle.append(levelOfPascal(i))
		return Triangle

#1.1
def levelOfPascal(num):
	if num == 1:
		return [1]
	elif num ==2:
		return [1,1]
	else:
		pre_level = levelOfPascal(num-1)
		for i in range(len(pre_level)-1):
			pre_level[i] = pre_level[i] + pre_level[i+1]
		level = [1] + pre_level
		return level



# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_numRows = [5]
	expected_output = [[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]]
	for i in range(len(input_numRows)):
		if generate(input_numRows[i]) != expected_output[i]:
			print("Wrong!!!")
			print(generate(input_numRows[i]))
		else:
			print("Right")		
	# print(generate(input1[-1]))
	

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