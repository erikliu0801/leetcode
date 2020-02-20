# ToDo:

"""
1022. Sum of Root To Leaf Binary Numbers
Easy

Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.

For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.

Return the sum of these numbers.

Example 1:

Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22 

Note:

    The number of nodes in the tree is between 1 and 1000.
    node.val is 0 or 1.
    The answer will not exceed 2^31 - 1.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
## test part
class Solution:
    def sumRootToLeaf(self, root):
        """
        root: TreeNode
        rtype: int
        """
## code here
#1
class Solution:
    def sumRootToLeaf(self, root):

    	def findLeaf(root): #recursive
			leaf = []
    		if root:
    			if root.left is None and root.right is None:
    				leaf += [root.val]
				else:
					findLeaf(root.left)
					findLeaf(root.right)
			return leaf

		def findLeaf(root): #iterative
			leaf = []
			nodes = [root]
			visited = 0
			while visited != len(nodes):
				node = nodes[visited] 
				if node:
					if node.left is None and node.right is None:
						leaf.append(node.val)
					else:
						nodes.append(node.left)
						nodes.append(node.right)
				visited += 1
			return leaf

		def rootToLeaf(root):
			root_leaf_s = []
			root_leaf = []

			if root:				
				root_leaf_s_l, root_leaf_l = rootToLeaf(root.left)
				root_leaf_s_r, root_leaf_r = rootToLeaf(root.left)
				root_leaf_s = root_leaf_s_l + root_leaf_s_r
				root_leaf = [root] + root_leaf_l + root_leaf_r
				if root.left is None and root.right is None:
					root_leaf_s += [root_leaf]
					
			return root_leaf_s, root_leaf

#1.1

class Solution:
    def sumRootToLeaf(self, root):

    	def rootToLeaf(root):
			root_leaf_s = []
			root_leaf = []

			if root:				
				root_leaf_s_l, root_leaf_l = rootToLeaf(root.left)
				root_leaf_s_r, root_leaf_r = rootToLeaf(root.left)
				root_leaf_s = root_leaf_s_l + root_leaf_s_r
				root_leaf = [root] + root_leaf_l + root_leaf_r
				if root.left is None and root.right is None:
					root_leaf_s += [root_leaf]
					
			return root_leaf_s, root_leaf



                



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
            print("Wrong!!!", ' Output:', func(input1[i]), '; Expected Output:', expected_output[i])
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