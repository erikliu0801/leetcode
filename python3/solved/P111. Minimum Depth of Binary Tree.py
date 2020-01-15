# ToDo:

"""
111. Minimum Depth of Binary Tree
Easy
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

"""
# Conditions & Concepts
"""
adjust from maxDepth() & levelOrderBottom()
def maxDepth(root):
	if type(root) != TreeNode:
		return 0
	else:
		checked_treenode, depth = 0, 0
		treenode_list = [root]
		while checked_treenode != len(treenode_list):
			alive_node = len(treenode_list)
			level_treenode = treenode_list[checked_treenode:]			
			for node in level_treenode:
				if node != None:
					if node.left != None:
						treenode_list.append(node.left)
					else:
						treenode_list.append(None)
					if node.right != None:
						treenode_list.append(node.right)
					else:
						treenode_list.append(None)
				checked_treenode += 1
			if len(treenode_list) > alive_node:
				depth += 1
		return depth

def levelOrderBottom(root):
	if type(root) != TreeNode:
		return []
	else:
		checked_treenode, k, dead_num = 0, 0, 0
		treenode_list, level_nums= [root], []
		while checked_treenode != len(treenode_list):
			level_treenode = treenode_list[checked_treenode:]
			level_nums.append(len(level_treenode)-dead_num)
			dead_num = 0
			for treenode in level_treenode:
				if treenode != None:
					if treenode.left != None:
						treenode_list.append(treenode.left)
					else:
						treenode_list.append(None)
						dead_num += 1
					if treenode.right != None:
						treenode_list.append(treenode.right)
					else:
						treenode_list.append(None)
						dead_num += 1
				checked_treenode += 1
			k += 1
		pass

"""
# Code
## submit part
class Solution:
    def minDepth(self, root: TreeNode) -> int:
## test part
def minDepth(root):
	"""
	root: TreeNode
	rtype: int
	"""
## code here
#1
"""
Success
Runtime: 40 ms, faster than 92.19% of Python3 online submissions for Minimum Depth of Binary Tree.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Minimum Depth of Binary Tree.
"""
def minDepth(root):
	if type(root) != TreeNode:
		return 0
	else:
		checked_treenode, depth, leaf_end = 0, 0, False
		treenode_list = [root]
		while leaf_end != True:
			alive_node = len(treenode_list)
			level_treenode = treenode_list[checked_treenode:]			
			for node in level_treenode:
				if node != None:
					if node.left == None and node.right == None:
						leaf_end = True
						break
					if node.left != None:
						treenode_list.append(node.left)
					else:
						treenode_list.append(None)
					if node.right != None:
						treenode_list.append(node.right)
					else:
						treenode_list.append(None)
				checked_treenode += 1
			depth += 1
		return depth

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