# ToDo:

"""
100. Same Tree
Easy

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
Example 2:

Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false
Example 3:

Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
## test part
def isSameTree(p, q):
	"""
	p: TreeNode
	q: TreeNode
	rtype: bool
	"""
## code here
#1
def isSameTree(p, q):

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	class TreeNode:
		def __init__(self, x):
			self.val = x
			self.left = None
			self.right = None
	def List2TreeNode:
		pass
	def TreeNode2List:
		pass
	input1 = [[1,2,3], [1,2], [1,2,1]]
	input2 = [[1,2,3], [1, null, 2], [1,1,2]]
	expected_output = [True, False, False]
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