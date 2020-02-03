# ToDo:

"""
501. Find Mode in Binary Search Tree
Easy

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

For example:
Given BST [1,null,2,2],

   1
	\
	 2
	/
   2


return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""
# Conditions & Concepts
"""
node.right.val >= node.val
node.left.val <= node.val

recursive solution
val_count: {str(val):count} #type:dict

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
	def findMode(self, root: TreeNode) -> List[int]:
		
## test part
def findMode(root):
	"""
	root: TreeNode
	rtype: List[int]
	"""
## code here
#1
def helper(root, val_count):
	val_count = dict()
	if root:
		helper(root.left)
		helper(root.right)
		index = str(root.val)
		if index in val_count:
			val_count[index] += 1
		else:
			val_count[index] = 1

def findMode(root):
	_, val_count = helper(root)
	if val_count.count(max(val_count)) == 1:
		


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