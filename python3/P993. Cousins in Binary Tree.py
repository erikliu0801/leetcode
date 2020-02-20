# ToDo:

"""
993. Cousins in Binary Tree
Easy

In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.

Note:
    The number of nodes in the tree will be between 2 and 100.
    Each node has a unique integer value from 1 to 100.

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
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
## test part
class Solution:
    def isCousins(self, root, x, y):
        """
        root: TreeNode
        x: int
        y: int
        rtype: bool
        """

## code here
#1 Same Generation
"""
Wrong Answer
Input: [1,2,3,null,4], 2, 3 #brothers
Output: true
Expected: false
"""
        def levelorder(root):
            if not root: return []
            
            #
            node_list = [[root]]
            checked = 0
            while checked != len(node_list):
                level = []
                for node in node_list[checked]:
                    if node:                        
                        if node.left: level += [node.left]
                        if node.right: level += [node.right]
                	if level: node_list += [level]
                checked += 1
            
            #
            vals_list = []
            for l in node_list:
                level = []
                for node in l:
                    level += [node.val]
                vals_list += [level]

            return vals_list

        vals = levelorder(root)
        for level in vals:
            if x in level or y in level:
                if x in level and y in level: return True
                else: return False
        return False

#1.1
class Solution:
    def isCousins(self, root, x, y):

        def levelorder(root): #by level, by node
			nodes = [[root]]
			visited = 0 #level
			while visited != len(nodes):
				by_level = []
				for l in nodes:
					by_node = []
					for node in l:
						if node:
							by_node.append(node.left)
							by_node.append(node.right)
					by_level.append(by_node)
				nodes.append(by_level)
				visited += 1
			return nodes


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