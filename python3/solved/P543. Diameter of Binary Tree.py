# ToDo:

"""
543. Diameter of Binary Tree
Easy

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree

          1
         / \
        2   3
       / \     
      4   5    

Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them. 
"""
# Conditions & Concepts
"""
res = length(root.left) + length(root.right)
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
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
## test part
def diameterOfBinaryTree(root):
	"""
	root: TreeNode
	rtype: int
	"""
## code here
#1
"""
Wrong Answer
Input: [4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
Output: 7
Expected: 8

Success
Runtime: 680 ms, faster than 6.52% of Python3 online submissions for Diameter of Binary Tree.
Memory Usage: 15.4 MB, less than 93.10% of Python3 online submissions for Diameter of Binary Tree.
"""
def diameterOfBinaryTree(root):
	
	def maxDepth(node):
		if not node:
			return 0
		depth_l = maxDepth(node.left)
		depth_r = maxDepth(node.right)
		return max(depth_l, depth_r) + 1
	
	if not root:
		return 0

	d = maxDepth(root.left) + maxDepth(root.right)
	return max(d, diameterOfBinaryTree(root.left), diameterOfBinaryTree(root.right))

	


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