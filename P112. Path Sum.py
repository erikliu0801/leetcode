# ToDo:

"""
112. Path Sum
Easy
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

	  5
	 / \
	4   8
   /   / \
  11  13  4
 /  \	  \
7	2	  1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

"""
# Conditions & Concepts
"""
1. find every leaf
1.1 preOrderTraversal
2. find sum of every leaf
3. cmp

adjust from minDepth()
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
"""
# Code
## submit part
class Solution:
	def hasPathSum(self, root: TreeNode, sum: int) -> bool:

## test part
def hasPathSum(root, sum):
	"""
	root: TreeNode
	sum: int
	rtype: bool
	"""

## code here
#1 find the all sum of leafs
"""
adjust from preOrderTraversal()
https://www.tutorialspoint.com/python_data_structure/python_tree_traversal_algorithms.htm
def preOrderTraversal(root):
	res = []
	if root:
		res.append(root.val)
		res = res + preOrderTraversal(root.left)
		res = res + preOrderTraversal(root.right)
	return res
"""
def pathSum(root):
	leaf = []
	if root:
		leaf.append(root.val)
		leaf = leaf + pathSum(root.left)		
		leaf = leaf + pathSum(root.right)
	return leaf_sum

#1.2


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