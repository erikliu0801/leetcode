# ToDo:
# Performance is too bad, need to be optimized!
"""
107. Binary Tree Level Order Traversal II
Easy

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its bottom-up level order traversal as:

[
  [15,7],
  [9,20],
  [3]
]


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
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
## test part
def levelOrderBottom(root):
	"""
	root: TreeNode
	rtype: List[List[int]]
	"""
## code here
#1
"""
Success
Runtime: 80 ms, faster than 5.38% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal II.
"""
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
		#
		for _ in range(len(level_nums)):
			if level_nums[-1] == 0:
				level_nums.pop(-1)
			else:
				break
		#
		while treenode_list.count(None) != 0:
			treenode_list.remove(None)
		#
		for i in range(len(level_nums)):
			level_val=[]
			for _ in range(level_nums[i]):
				level_val.append(treenode_list[0].val)
				treenode_list.pop(0)
			level_nums[i] = level_val
		return level_nums.reverse()

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
	expected_output = [[[15,7],[9,20],[3]]]
	for i in range(len(input_nums)):
		if levelOrderBottom(List2TreeNode(input_nums[i])) != expected_output[i]:
			print("Wrong!!!")
			print(levelOrderBottom(List2TreeNode(input_nums[i])))
		else:
			print("Right")		
	# print(levelOrderBottom(List2TreeNode(input_nums[-1])))
	

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