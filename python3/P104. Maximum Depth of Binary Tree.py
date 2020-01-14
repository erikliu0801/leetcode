# ToDo:

"""
104. Maximum Depth of Binary Tree
Easy

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its depth = 3.


"""
# Conditions & Concepts
"""
#adjust from levelOrderTraversal()
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
# Code
## submit part
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
## test part
def maxDepth(root):
	"""
	root: TreeNode
	rtype: int
	"""
## code here
#1
"""
Success
Runtime: 36 ms, faster than 95.21% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Maximum Depth of Binary Tree.
"""
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

	def List2TreeNode(nums):
		"""
		nums: List
		rtype: highest TreeNode
		"""
		if len(nums)==0:
			return
		else:
			alive_node, checked_num = 0, 1 #int: by level
			treenode = [TreeNode(nums[0])]
			while alive_node != len(treenode):
				level_treenode = treenode[alive_node:] #list
				if checked_num <= len(nums):
					rest_nums = nums[checked_num:]
				else:
					break
				for i in range(len(level_treenode)):			
					if i*2 <= len(rest_nums) -1 :
						if rest_nums[i*2] != None:
							treenode[alive_node].left = TreeNode(rest_nums[i*2])
							treenode.append(treenode[alive_node].left)
					if i*2 <= len(rest_nums) -2 :
						if rest_nums[i*2+1] != None:
							treenode[alive_node].right = TreeNode(rest_nums[i*2+1])
							treenode.append(treenode[alive_node].right)
					checked_num += 2
					alive_node += 1
			return treenode[0]

	def TreeNode2List(tree_node):
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
			for i in range(len(treenode_list)):
				if treenode_list[i] != None:
					treenode_list[i] = treenode_list[i].val
			return treenode_list

	input_nums = [[3,9,20,None,None,15,7]]
	expected_output = [3]
	for i in range(len(input_nums)):
		if maxDepth(List2TreeNode(input_nums[i])) != expected_output[i]:
			print("Wrong!!!")
			print(maxDepth(List2TreeNode(input_nums[i])))
		else:
			print("Right")		
	# print(maxDepth(List2TreeNode(input_nums[-1])))
	

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