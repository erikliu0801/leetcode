# ToDo:

"""
257. Binary Tree Paths
Easy

1182

82

Add to List

Share
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2	 3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
Accepted
266.6K
Submissions
551.3K
Seen this question in a real interview before?

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
	def binaryTreePaths(self, root: TreeNode) -> List[str]:
		
## test part
def binaryTreePaths(root):
	"""
	root: TreeNode
	rtype: List[str]
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
def binaryTreePaths(root):
	leaf_s = []
	if root:
		leaf_s_left = binaryTreePaths(root.left)
		leaf_s_right = binaryTreePaths(root.right)
		leaf_s = leaf_s + leaf_s_left + leaf_s_right
		if root.left == None and root.right == None:
			leaf_s.append([root])
		for i, leaf in enumerate(leaf_s):
			if root.left in leaf or root.right in leaf:
				leaf_s[i].insert(0,root)
	return leaf_s

#1.1
"""
Your input: [1,2,3,null,5]
Output: [[1,2,5],[1,3]]
Expected: ["1->2->5","1->3"]

Success
Runtime: 32 ms, faster than 75.31% of Python3 online submissions for Binary Tree Paths.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Binary Tree Paths.
"""
def binaryTreePaths(root):
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
	_, leaf_s_val = leafPath(root)
	for i, leaf_val in enumerate(leaf_s_val):
		leaf_str = str(leaf_val[0])
		for node_val in leaf_val[1:]:
			leaf_str = leaf_str + '->' + str(node_val)
		leaf_s_val[i] = leaf_str
	return leaf_s_val


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