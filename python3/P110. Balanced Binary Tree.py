# ToDo:

"""
110. Balanced Binary Tree
Easy

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

	3
   / \
  9  20
	/  \
   15   7
Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

	   1
	  / \
	 2   2
	/ \
   3   3
  / \
 4   4
Return false.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, x):
#		 self.val = x
#		 self.left = None
#		 self.right = None


class Solution:
	def isBalanced(self, root: TreeNode) -> bool:
## test part
def isBalanced(root):
	"""
	root: TreeNode
	rtype: bool
	"""
## code here
#1
# def isBalanced(root):
# 	depth_l, depth_r = 0, 0
# 	root_l, root_r = root, root
# 	while root_l.left:
# 		depth_l += 1
# 		root_l = root_l.left
# 	while root_r.right:
# 		depth_r += 1
# 		root_r = root_l.right
# 	if depth_l > depth_r +1 or depth_l +1 < depth_r:
# 		return False
# 	return True

#2
# def isBalanced(root):
# 	def maxDepth(root):
# 		depth = 1
# 		if not root:
# 			depth = 0
# 			return depth
# 		if root.left and root.right:
# 			depth_l = maxDepth(root.left)
# 			depth_r = maxDepth(root.right)
# 			return max(depth_l, depth_r) + 1
# 	depth_l , depth_r = maxDepth(root.left),  maxDepth(root.right)
# 	if depth_l > depth_r +1 or depth_l +1 < depth_r:
# 		return False
# 	return True

#2.1
"""
[]

Wrong Answer
Input: [1,2,2,3,null,null,3,4,null,null,4]
Output: true
Expected: false

every node!!!  differ in height by no more than 1.
"""
def isBalanced(root):
	def maxDepth(_root):
		if not _root: 
			return 0
		depth_l = maxDepth(_root.left)
		depth_r = maxDepth(_root.right)
		return max(depth_l, depth_r) + 1
	if type(root) is not TreeNode:
		return True
	depth_l , depth_r = maxDepth(root.left),  maxDepth(root.right)
	if depth_l > depth_r +1 or depth_l +1 < depth_r:
		return False
	return True

#3
"""
Wrong Answer
Your input: [1,2,2,3,3,null,null,4,4]
Output: true
Expected: false
"""
def isBalanced(root):
	if not root:
		return True
	if root.right is None and root.left is not None:
		if root.left.left is not None or root.left.right is not None:
			return False
	if root.left is None and root.right is not None:
		if root.right.left is not None or root.right.right is not None:
			return False
	return isBalanced(root.left) and isBalanced(root.right)




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