# ToDo:

"""
101. Symmetric Tree
Easy

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

 

Note:
Bonus points if you could solve it both recursively and iteratively.
"""
# Conditions & Concepts
"""
# make mirror
# comp mirror
"""
# Code
## submit part
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
## test part
def isSymmetric(root):
	"""
	root: TreeNode
	rtype: bool
	"""
## code here
#1
def isSymmetric(root):
	def mirrorTree(root):
		if type(root) != TreeNode:
			return 
		else:
			checked_treenode = 0
			treenode_list = [root]
			while checked_treenode != len(treenode_list):
				level_treenode = treenode_list[checked_treenode:]
				for tree_node in level_treenode:
					if tree_node != None:
						if tree_node.left == None and tree_node.right == None:
							pass
						elif tree_node.left != None or tree_node.right != None:
							_ = tree_node.left
							tree_node.left, tree_node = tree_node.right, _
							if tree_node.left != None:
								treenode_list.append(tree_node.left)
							if tree_node.right != None:
								treenode_list.append(tree_node.right)
					checked_treenode += 1
			return root
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
	mirror_tree = mirrorTree(root)
	if not mirror_tree:
		return True
	else:
		if TreeNode2List(root) != TreeNode2List(mirror_tree):
			return False
		else:
			return True

#1.1 
def mirrorTree(tree_node):
	if type(tree_node) != TreeNode:
		return 
	else:
		checked_treenode = 0
		treenode_list = [tree_node]
		while checked_treenode != len(treenode_list):
			level_treenode = treenode_list[checked_treenode:]
			for node in level_treenode:
				if node != None:
					if node.left == None and node.right == None:
						pass
					elif node.left != None or node.right != None:
						_ = node.left
						node.left, node = node.right, _
						if node.left != None:
							treenode_list.append(node.left)
						if node.right != None:
							treenode_list.append(node.right)
				checked_treenode += 1
		return treenode_list[0]


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

	input_treenode = [
	[1,2,2,3,4,4,3],
	[1,2,2,None,3,None,3]]
	expected_output = [True, False]
	for i in range(len(input_treenode)):
		if isSymmetric(List2TreeNode(input_treenode[i])) != expected_output[i]:
			print("Wrong!!!")
			print(isSymmetric(List2TreeNode(input_treenode[i])))
		else:
			print("Right")		
	# print(isSymmetric(List2TreeNode(input_treenode[-1])))
	

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