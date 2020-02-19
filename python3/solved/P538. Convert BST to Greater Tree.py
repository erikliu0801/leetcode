# ToDo:

"""
538. Convert BST to Greater Tree
Easy

Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:

Input: The root of a Binary Search Tree like this:
			  5
			/   \
		   2	 13

Output: The root of a Greater Tree like this:
			 18
			/   \
		  20	 13
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
# Definition for a binary tree node.
# class TreeNode:
# 	def __init__(self, x):
# 		self.val = x
# 		self.left = None
# 		self.right = None

class Solution:
	def convertBST(self, root: TreeNode) -> TreeNode:
		
## test part
def convertBST(root):
	"""
	root: TreeNode
	rtype: TreeNode
	"""
## code here
#1
"""
Success
Runtime: 9436 ms, faster than 5.06% of Python3 online submissions for Convert BST to Greater Tree.
Memory Usage: 15.6 MB, less than 87.50% of Python3 online submissions for Convert BST to Greater Tree.
"""
def convertBST(root):
	def preOrderTraversal(node):
		res = []
		obj = []
		if node:
			res.append(node.val)
			obj.append(node)
			res_l, obj_l = preOrderTraversal(node.left)
			res_r, obj_r = preOrderTraversal(node.right)
			res += res_l + res_r
			obj += obj_l + obj_r
		return res, obj

	vals, nodes = preOrderTraversal(root)
	from collections import Counter
	vals_count = Counter(vals)
	for i, val in enumerate(vals):
		for k in vals_count:
			if k > val:
				vals[i] += k*vals_count[k]

	for i in range(len(nodes)):
		nodes[i].val = vals[i]
	return root

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