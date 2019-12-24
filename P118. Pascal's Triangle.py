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
def generate(numRows):

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