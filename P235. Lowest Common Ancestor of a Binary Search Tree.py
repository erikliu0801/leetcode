# ToDo:

"""
235. Lowest Common Ancestor of a Binary Search Tree
Easy
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]


 

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
 

Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the BST.

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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
## test part
def lowestCommonAncestor(root, p, q):
	"""
	root: TreeNode
	p: TreeNode
	q: TreeNode
	rtype: TreeNode
	"""
## code here
#1
"""
ajdust from P112 leafPath(root)
def leafPath(root):			
	leaf_s, leaf_s_val = [], []
	if root:
		leaf_s_left, leaf_s_val_left = leafPath(root.left)
		leaf_s_right, leaf_s_val_right = leafPath(root.right)
		leaf_s, leaf_s_val = leaf_s + leaf_s_left + leaf_s_right, leaf_s_val + leaf_s_val_left + leaf_s_val_right
		if root.left == None and root.right == None:
			leaf_s.append([root])
			leaf_s_val.append([root.val])
		for i, leaf in enumerate(leaf_s):
			if root.left in leaf or root.right in leaf:
				leaf_s[i].insert(0,root)
				leaf_s_val[i].insert(0,root.val)
	return leaf_s, leaf_s_val
"""
def lowestCommonAncestor(root, p, q):
	leafeaf_s = []
	find = set([p,q]) #
	if root:
		leaf_s_left = leafPath(root.left)
		leaf_s_right = leafPath(root.right)
		leaf_s = leaf_s + leaf_s_left + leaf_s_right
		if root.left == None and root.right == None:
			leaf_s.append([root])
		for i, leaf in enumerate(leaf_s):
			if root.left in leaf or root.right in leaf:
				leaf_s[i].insert(0,root)
	return leaf_s


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