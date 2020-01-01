# ToDo:

"""
404. Sum of Left Leaves
Easy
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        
## test part
def sumOfLeftLeaves(root):
	"""
	root: TreeNode
	rtype: int
	"""
## code here
#1
"""
adjust from inOrderTraversal(root) and P112 hasPathSum(root, sum)
def inOrderTraversal(root):
    res = []
    if root:
        res = inOrderTraversal(root.left)
        res.append(root.val)
        res = res + inOrderTraversal(root.right)
    return res


def hasPathSum(root, sum):
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
	def leafPathSum(leaf_s_val):		
		for i, leaf in enumerate(leaf_s_val):
			leaf_sum = 0
			for val in leaf:
				leaf_sum += val
			leaf_s_val[i] = leaf_sum
		return leaf_s_val
	_, leaf_s_val = leafPath(root)
	leaf_sum = leafPathSum(leaf_s_val)
	if sum in leaf_sum:
		return True
	else:
		return False


Success
Runtime: 36 ms, faster than 50.00% of Python3 online submissions for Sum of Left Leaves.
Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Sum of Left Leaves.
"""
def leafPath(root):			
	leaf_s = []
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

def sumOfLeftLeaves(root):
	def leafPath(root):			
		leaf_s = []
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
	if root is None:
		return 0
	if root.left is None and root.right is None:
		return 0
	left_leaves_sum = 0
	leaf_s = leafPath(root)
	for leaf in leaf_s:
		if leaf[-2].left == leaf[-1]:
			left_leaves_sum += leaf[-1].val
	return left_leaves_sum


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