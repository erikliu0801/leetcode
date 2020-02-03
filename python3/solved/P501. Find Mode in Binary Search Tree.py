# ToDo:

"""
501. Find Mode in Binary Search Tree
Easy

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

For example:
Given BST [1,null,2,2],

	1
	\
	 2
	/
   2


return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""
# Conditions & Concepts
"""
node.right.val >= node.val
node.left.val <= node.val

recursive solution
val_count: {str(val):count} #type:dict

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
	def findMode(self, root: TreeNode) -> List[int]:
		
## test part
def findMode(root):
	"""
	root: TreeNode
	rtype: List[int]
	"""
## code here
#1
"""
Success
Runtime: 80 ms, faster than 10.10% of Python3 online submissions for Find Mode in Binary Search Tree.
Memory Usage: 16.9 MB, less than 100.00% of Python3 online submissions for Find Mode in Binary Search Tree.
"""
def findMode(root):
	def helper(root):
		val_count = dict()
		if root:
			_, val_count = helper(root.left)
			_, val_count1 = helper(root.right)
			for k in val_count:
				if k in val_count1:
					val_count[k] += val_count1[k]
					val_count1.pop(k)
			val_count.update(val_count1)
			index = str(root.val)
			if index in val_count:
				val_count[index] += 1
			else:
				val_count[index] = 1
		return root, val_count
	_, val_count = helper(root)
	max_count = 0
	mode = list()
	for k, v in val_count.items():
		if v > max_count:
			mode = [int(k)]
			max_count = v
		elif v == max_count:
			mode.extend([int(k)])
	return mode

#1.1
"""
key of dict can be int

"""
def findMode(root):
	def helper(root):
		val_count = dict()
		if root:
			_, val_count = helper(root.left)
			_, val_count1 = helper(root.right)
			#for k in val_count.keys() & val_count1.keys():
			#	val_count[k] += val_count1[k]
			#for k in val_count1.keys() - val_count.keys():
			#	val_count[k] = val_count1[k]
			val_count.update({k:val_count[k]+val_count1[k] for k in val_count1.keys() & val_count.keys()})
			val_count.update({k:val_count1[k] for k in val_count1.keys() - val_count.keys()})
			index = root.val
			if index in val_count:
				val_count[index] += 1
			else:
				#val_count.setdefault(index, default = 1)
				val_count[index] = 1
		return root, val_count
	_, val_count = helper(root)
	mode = list()
	max_count = max(val_count.values())
	while max_count == max(val_count.values()): #ValueError: max() arg is an empty sequence
		_, val = max(zip(val_count.values(),val_count.keys()))
		mode.append(val)
		val_count.pop(val)
	return mode

#2
def findMode(root):
	def postOrder(node):
		res = list()
		if node:
			res = postOrder(node.left)
			res = postOrder(node.right)
			res.append(node.val)
		return res

	from collections import Counter
	values = postOrder(root)
	val_count = Counter(values)
	



# Test
## Functional Test
"""
# Conditions & Concepts

"""


def main():
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

	def insert(self, val):
		if self.val:
			if data < self.val:
				if self.left is None:
					self.left = TreeNode(val)
				else:
					self.left.insert(val)
			elif data > self.val:
				if self.rifgt is None:
					self.right = TreeNode(val)
				else:
					self.right.insert(val)
		else:
			self.val = data
	root = 

	print()




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