# ToDo:

"""
100. Same Tree
Easy

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:	 1		 1
		  / \	   / \
		 2   3	 2   3

		[1,2,3],   [1,2,3]

Output: true
Example 2:

Input:	 1		 1
		  /		   \
		 2			 2

		[1,2],	 [1,null,2]

Output: false
Example 3:

Input:	 1		 1
		  / \	   / \
		 2   1	 1   2

		[1,2,1],   [1,1,2]

Output: false

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
	def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
## test part
def isSameTree(p, q):
	"""
	p: TreeNode
	q: TreeNode
	rtype: bool
	"""
## code here
#1
def isSameTree(p, q):
	def levelOrderTraversal(TreeNode):
		level_order_treenode = [TreeNode]
		n, last_len = 0, 0
		while last_len != len(level_order_treenode):
			last_len, m = len(level_order_treenode), n
			for i in range(len(level_order_treenode[m:])):
				if level_order_treenode[m+i].left != None:
					level_order_treenode.append(level_order_treenode[m+i].left)
				if level_order_treenode[m+i].right != None:
					level_order_treenode.append(level_order_treenode[m+i].right)
				n+=1
		return level_order_treenode
	p_list, q_list = levelOrderTraversal(p), levelOrderTraversal(q)
	if len(p_list) != len(q_list):
		return False
	for i in range(len(p_list)):
		if p_list[i].val != q_list[i].val:
			return False
	return True

#1.1 level-order traversal
"""
if only .left or .right
"""
def levelOrderTraversal(TreeNode):
	level_order_treenode = [TreeNode]
	n, last_len = 0, 0
	while last_len != len(level_order_treenode):
		last_len, m = len(level_order_treenode), n
		for i in range(len(level_order_treenode[m:])):
			if level_order_treenode[m+i].left != None:
				level_order_treenode.append(level_order_treenode[m+i].left)
			if level_order_treenode[m+i].right != None:
				level_order_treenode.append(level_order_treenode[m+i].right)
			n+=1
	return level_order_treenode

#1.2
"""
[1,2], [1,null,2]
[], []
[10,5,15], [10,5,null,null,15]
[2, null, 4], [2,3,4]
[0], [0]
[1, null, 2, 3], [1, null, 2, null, 3] => levelOrderTraversal()
[390,255,2266,-273,337,1105,3440,-425,4113,null,null,600,1355,3241,4731,-488,-367,16,null,565,780,1311,1755,3075,3392,4725,4817,null,null,null,null,-187,152,395,null,728,977,1270,null,1611,1786,2991,3175,3286,null,164,null,null,4864,-252,-95,82,null,391,469,638,769,862,1045,1138,null,1460,1663,null,1838,2891,null,null,null,null,3296,3670,4381,null,4905,null,null,null,-58,null,null,null,null,null,null,null,null,734,null,843,958,null,null,null,1163,1445,1533,null,null,null,2111,2792,null,null,null,3493,3933,4302,4488,null,null,null,null,null,null,819,null,null,null,null,1216,null,null,1522,null,1889,2238,2558,2832,null,3519,3848,4090,4165,null,4404,4630,null,null,null,null,null,null,1885,2018,2199,null,2364,2678,null,null,null,3618,3751,null,4006,null,null,4246,null,null,4554,null,null,null,1936,null,null,null,null,2444,2642,2732,null,null,null,null,null,null,null,4253,null,null,null,null,2393,2461,null,null,null,null,4250,null,null,null,null,2537], 
[390,255,2266,-273,337,1105,3440,-425,4113,null,null,600,1355,3241,4731,-488,-367,16,null,565,780,1311,1755,3075,3392,4725,4817,null,null,null,null,-187,152,395,null,728,977,1270,null,1611,1786,2991,3175,3286,null,164,null,null,4864,-252,-95,82,null,391,469,638,769,862,1045,1138,null,1460,1663,null,1838,2891,null,null,null,null,3296,3670,4381,null,4905,null,null,null,-58,null,null,null,null,null,null,null,null,734,null,843,958,null,null,null,1163,1445,1533,null,null,null,2111,2792,null,null,null,3493,3933,4302,4488,null,null,null,null,null,null,819,null,null,null,null,1216,null,null,1522,null,1889,2238,2558,2832,null,3519,3848,4090,4165,null,4404,4630,null,null,null,null,null,null,1885,2018,2199,null,2364,2678,null,null,null,3618,3751,null,4006,null,null,4246,null,null,4554,null,null,null,1936,null,null,null,null,2444,2642,2732,null,null,null,null,null,null,null,4253,null,null,null,null,2461,2393,null,null,null,null,4250,null,null,null,null,2537]
"""
def isSameTree(p, q):
	def levelOrderTraversal(TreeNode):
		"""
		rtype: left_list, right_list
		highest_treenode belongs to left_list
		"""
		level_order_treenode_left = [TreeNode]
		level_order_treenode_right = [None]
		m, last_len = 0, 0
		while last_len != len(level_order_treenode_left+level_order_treenode_right):
			last_len= len(level_order_treenode_left+level_order_treenode_right)
			level_order_treenode = level_order_treenode_left[m:] + level_order_treenode_right[m:]
			for i in range(len(level_order_treenode)):
				if level_order_treenode[i]!= None:
					if level_order_treenode[i].left != None:
						level_order_treenode_left.append(level_order_treenode[i].left)
					else:
						level_order_treenode_left.append(None)
					if level_order_treenode[i].right != None:
						level_order_treenode_right.append(level_order_treenode[i].right)
					else:
						level_order_treenode_left.append(None)
				m += 1
		return level_order_treenode_left, level_order_treenode_right[1:]

	if p is None or q is None:
		if p is None and q is None:
			return True
		else:
			return False
	else:
		p_list_left, p_list_right = levelOrderTraversal(p)
		q_list_left, q_list_right = levelOrderTraversal(q)
		if len(p_list_left) != len(q_list_left) or len(p_list_right) != len(q_list_right):
			return False
		p_list, q_list = p_list_left + p_list_right, q_list_left + q_list_right
		for i in range(len(p_list)):
			if p_list[i]!= None and q_list[i]!= None:
				if p_list[i].val != q_list[i].val:
					return False
			elif p_list[i] != q_list[i]:
				return False
		return True

#1.3
def levelOrderTraversal(TreeNode):
	"""
	rtype: left_list, right_list
	highest_treenode belongs to left_list
	"""
	level_order_treenode_left = [TreeNode]
	level_order_treenode_right = [None]
	m, last_len = 0, 0
	while last_len != len(level_order_treenode_left+level_order_treenode_right):
		last_len= len(level_order_treenode_left+level_order_treenode_right)
		if m == 0 :
			level_order_treenode = level_order_treenode_left
		else:
			level_order_treenode = level_order_treenode_left[m:] + level_order_treenode_right[m:]
		for i in range(len(level_order_treenode)):
			if level_order_treenode[i]!= None:
				if level_order_treenode[i].left != None:
					level_order_treenode_left.append(level_order_treenode[i].left)
				else:
					level_order_treenode_left.append(None)
				if level_order_treenode[i].right != None:
					level_order_treenode_right.append(level_order_treenode[i].right)
				else:
					level_order_treenode_left.append(None)
			m += 1
	return level_order_treenode_left, level_order_treenode_right[1:]

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
			checked_num = 0 #level
			treenode = [TreeNode(nums[0])]
			while checked_num != len(treenode):
				level_nums=nums[checked_num:]
				for i in range(len(level_nums)):
					if i+1<= len(level_nums) and level_nums[i+1] != None:
						treenode[l].left = TreeNode(level_nums[i+1])
						treenode.append(treenode[l].left)

					if i+2<= len(level_nums) and level_nums[i+2] != None:
						treenode[l].right = TreeNode(level_nums[i+2])
						treenode.append(treenode[l].right)
				checked_num += 1
			return 1st_treenode





	def TreeNode2List(TreeNode):
		if type(TreeNode) != TreeNode:
			return []
		else:
			pass

	input_p_list = [
	[1,2],
	[],
	[10,5,15],
	[2, None, 4],
	[0],
	[1,None,2,3],
	[390,255,2266,-273,337,1105,3440,-425,4113,None,None,600,1355,3241,4731,-488,-367,16,None,565,780,1311,1755,3075,3392,4725,4817,None,None,None,None,-187,152,395,None,728,977,1270,None,1611,1786,2991,3175,3286,None,164,None,None,4864,-252,-95,82,None,391,469,638,769,862,1045,1138,None,1460,1663,None,1838,2891,None,None,None,None,3296,3670,4381,None,4905,None,None,None,-58,None,None,None,None,None,None,None,None,734,None,843,958,None,None,None,1163,1445,1533,None,None,None,2111,2792,None,None,None,3493,3933,4302,4488,None,None,None,None,None,None,819,None,None,None,None,1216,None,None,1522,None,1889,2238,2558,2832,None,3519,3848,4090,4165,None,4404,4630,None,None,None,None,None,None,1885,2018,2199,None,2364,2678,None,None,None,3618,3751,None,4006,None,None,4246,None,None,4554,None,None,None,1936,None,None,None,None,2444,2642,2732,None,None,None,None,None,None,None,4253,None,None,None,None,2393,2461,None,None,None,None,4250,None,None,None,None,2537]]
	input_q_list = [
	[1,None,2],
	[],
	[10,5,None,None,15],
	[2,3,4],
	[0],
	[1,None,2,None,3],
	[390,255,2266,-273,337,1105,3440,-425,4113,None,None,600,1355,3241,4731,-488,-367,16,None,565,780,1311,1755,3075,3392,4725,4817,None,None,None,None,-187,152,395,None,728,977,1270,None,1611,1786,2991,3175,3286,None,164,None,None,4864,-252,-95,82,None,391,469,638,769,862,1045,1138,None,1460,1663,None,1838,2891,None,None,None,None,3296,3670,4381,None,4905,None,None,None,-58,None,None,None,None,None,None,None,None,734,None,843,958,None,None,None,1163,1445,1533,None,None,None,2111,2792,None,None,None,3493,3933,4302,4488,None,None,None,None,None,None,819,None,None,None,None,1216,None,None,1522,None,1889,2238,2558,2832,None,3519,3848,4090,4165,None,4404,4630,None,None,None,None,None,None,1885,2018,2199,None,2364,2678,None,None,None,3618,3751,None,4006,None,None,4246,None,None,4554,None,None,None,1936,None,None,None,None,2444,2642,2732,None,None,None,None,None,None,None,4253,None,None,None,None,2461,2393,None,None,None,None,4250,None,None,None,None,2537]]
	expected_output = [False, True, False, False, True, False, False]
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