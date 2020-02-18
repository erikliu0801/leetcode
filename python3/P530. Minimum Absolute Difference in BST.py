# ToDo:

"""
530. Minimum Absolute Difference in BST
Easy

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.


Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
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
	def getMinimumDifference(self, root: TreeNode) -> int:
		
## test part
def getMinimumDifference(root):
	"""
	root: TreeNode
	rtype: int
	"""
## code here
#1
"""
Wrong Answer
Input: [236,104,701,null,227,null,911]
Output: 123
Expected: 9
"""
# def getMinimumDifference(root):
# 	d = float('inf')
# 	if root:
# 		if root.left != None:
# 			d = min(d, abs(root.val - root.left.val))
# 		if root.right != None:
# 			d = min(d, abs(root.val - root.right.val))
# 		d = min(d, getMinimumDifference(root.left), getMinimumDifference(root.right))
# 	return d

#1.1
"""
Time Limit Exceeded
186 / 186 test cases passed, but took too long.
"""
def getMinimumDifference(root):
	def preOrderTraversal(node):
		res = []
		if node:
			res.append(node.val)
			res = res + preOrderTraversal(node.left)
			res = res + preOrderTraversal(node.right)
		return res
	val_s = preOrderTraversal(root)
	d = float('inf')
	for i in range(len(val_s)-1):
		for y in val_s[i+1:]:
			d = min(d, abs(val_s[i]-y))
	return d


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