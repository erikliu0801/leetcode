# ToDo:

"""
687. Longest Univalue Path
Easy

Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

Example 1:
Input:

      5
     / \
    4   5
   / \   \
  1   1   5

Output: 2

Example 2:
Input:

      1
     / \
    4   5
   / \   \
  4   4   5

Output: 2

Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        
## test part
class Solution:
    def longestUnivaluePath(self, root):
    	"""
    	root: TreeNode
    	rtype: int
    	"""
## code here
#1
class Solution:
    def longestUnivaluePath(self, root):

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