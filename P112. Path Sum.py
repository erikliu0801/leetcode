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
 /  \      \
7    2      1
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
def pathSum(root):
	"""
	root: TreeNode
	rtype: List[int]
	"""
	if type(root) != TreeNode:
		return 
	else:
		checked_treenode, leaf_num, leaf = 0, 0, []
		treenode_list = [root]
		while expression:
			alive_node = len(treenode_list)
			level_treenode = treenode_list[checked_treenode:]			
			for node in level_treenode:
				if node != None:
					if node.left == None and node.right == None:
						# leaf = leaf.append(node.val)
						leaf_num += 1
					if node.left != None:
						treenode_list.append(node.left)
					else:
						treenode_list.append(None)
					if node.right != None:
						treenode_list.append(node.right)
					else:
						treenode_list.append(None)
				checked_treenode += 1
		return leaf

#1.1
"""
adjust from levelOrderTraversal()
def levelOrderTraversal(tree_node):
	if type(tree_node) != TreeNode:
			return []
	else:
		checked_treenode = 0
		treenode_list = [tree_node]
		while checked_treenode != len(treenode_list):
			level_treenode = treenode_list[checked_treenode:]
			for treenode in level_treenode:
				if treenode != None:
					if treenode.left != None:
						treenode_list.append(treenode.left)
					else:
						treenode_list.append(None)
					if treenode.right != None:
						treenode_list.append(treenode.right)
					else:
						treenode_list.append(None)
				checked_treenode += 1
		for _ in range(len(treenode_list)):
			if treenode_list[-1] == None:
				treenode_list.pop(-1)
			else:
				break
		return treenode_list
"""
def preOrderTraversal(root):
	if type(root) != TreeNode:
		return []
	else:
		checking_num, checked_node = 0, []
		before_checked_num = 0
		leaf_list, leaf_s_list = [root], []
		while root:
			while leaf_list[checking_num].left != None:
				leaf_list.append(leaf_list[checking_num].left)
				checking_num += 1
			leaf_s_list.append(leaf_list)
			while leaf_list[checking_num].right == None or leaf_list[checking_num].right in checked_node: #
				if leaf_list[checking_num] == root:
					break
				if leaf_list[checking_num] not in checked_node:
					checked_node.append(leaf_list[checking_num])
				checking_num -= 1
			if leaf_list[checking_num] == root: #
				break
			leaf_list = leaf_list[:checking_num+1]
			leaf_list.append(leaf_list[checking_num].right)
			checking_num += 1
		return leaf_s_list


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