# ToDo:

"""
119. Pascal's Triangle II
Easy

Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]

Follow up:

Could you optimize your algorithm to use only O(k) extra space?


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        else:
            pre_level = self.getRow(rowIndex-1)
            for i in range(len(pre_level)-1):
                pre_level[i] = pre_level[i] + pre_level[i+1]
            level = [1] + pre_level
            return level
## test part
def getRow(rowIndex):
	"""
	rowIndex: int
	rtype: List[int]
	"""
## code here
#1
"""
adjust from P118 levelOfPascal()
start from 0
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

Success
Runtime: 24 ms, faster than 95.13% of Python3 online submissions for Pascal's Triangle II.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Pascal's Triangle II.
"""
def getRow(rowIndex):
	if rowIndex == 0:
		return [1]
	elif rowIndex == 1:
		return [1,1]
	else:
		pre_level = getRow(rowIndex-1)
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
	input1 = []
	expected_output = []
	for i in range(len(input1)):
		if func(input1[i]) != expected_output[i]:
			print("Wrong!!!")
			print(func(input1[i]))
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