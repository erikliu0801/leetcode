# ToDo:

"""
108. Convert Sorted Array to Binary Search Tree
Easy

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5



"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
## test part
def sortedArrayToBST(nums):
	"""
	nums: List[int]
	rtype: TreeNode
	"""
## code here
#1
"""
input: [0,1,2,3,4,5]
output: [3,2,4,1,null,null,5,0]
expected: [3,1,5,0,2,4] => bug?

"""
def sortedArrayToBST(nums):
	if len(nums)==0:
		return
	else:
		middle = len(nums)//2
		root = TreeNode(nums[middle])
		tree_left = nums[:middle] #exclude root
		tree_left.reverse() #tree_left = nums[:middle+1].reverse() will return None
		tree_right = nums[middle+1:] #exclude root
		tree_left.insert(0, root) #include root
		tree_right.insert(0, root) #include root
		for i in range(len(tree_left)-1):
			tree_left[i].left = TreeNode(tree_left[i+1])
			tree_left[i+1] = tree_left[i].left
		for i in range(len(tree_right)-1):
			tree_right[i].right = TreeNode(tree_right[i+1])
			tree_right[i + 1] = tree_right[i].right
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

	input_nums = [[-10,-3,0,5,9], [0,1,2,3,4,5]]
	expected_output = []
	# for i in range(len(input_nums)):
	# 	if sortedArrayToBST(input_nums[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(sortedArrayToBST(input_nums[i]))
	# 	else:
	# 		print("Right")
	print(sortedArrayToBST(input_nums[-1]))
	

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