# ToDo:

"""
226. Invert Binary Tree
Easy
Invert a binary tree.

Example:

Input:

	 4
   /   \
  2	 7
 / \   / \
1   3 6   9
Output:

	 4
   /   \
  7	 2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

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
	def invertTree(self, root: TreeNode) -> TreeNode:
		
## test part
def invertTree(root):
	"""
	root: TreeNode
	rtype: TreeNode
	"""
## code here
#1
"""
mirrorTree(tree_node) in P101

Success
Runtime: 28 ms, faster than 81.81% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Invert Binary Tree.
"""
def invertTree(root):
	if type(root) != TreeNode:
		return 
	else:
		checked_treenode = 0
		treenode_list = [root]
		while checked_treenode != len(treenode_list):
			level_treenode = treenode_list[checked_treenode:]
			for node in level_treenode:
				if node != None:
					if node.left == None and node.right == None:
						pass
					elif node.left != None or node.right != None:
						_ = node.left
						node.left, node.right = node.right, _
						if node.left != None:
							treenode_list.append(node.left)
						if node.right != None:
							treenode_list.append(node.right)
				checked_treenode += 1
		return root


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
	
		def PrintTree(self):
			if self.left:
				self.left.PrintTree()
			print(self.val),
			if self.right:
				self.right.PrintTree()

		def insert(self, val):
			if self.val:				
				if self.left is None and self.left is not None:
					self.left = TreeNode(val)
				elif self.left is not None and self.left is not None::
					self.left.insert(val)
			else:
				self.val = val

	#226
	input_nums = [[4, 2, 7, 1, 3, 6, 9]]
	for nums in input_nums:
		root = TreeNode(nums[0])
		for i in nums[1:]:
			root.insert(i)
	root.PrintTree()
	

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