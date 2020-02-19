# ToDo:

"""
700. Search in a Binary Search Tree
Easy

Given the root node of a binary search tree (BST) and a value. You need to find the node in the BST that the node's value equals the given value. Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

For example, 

Given the tree:
        4
       / \
      2   7
     / \
    1   3

And the value to search: 2

You should return this subtree:

      2     
     / \   
    1   3

In the example above, if we want to search the value 5, since there is no node with value 5, we should return NULL.

Note that an empty tree is represented by NULL, therefore you would see the expected output (serialized tree format) as [], not null.


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
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
## test part
class Solution:
    def searchBST(self, root, val):
        """
        root: TreeNode
        val: int
        rtype: TreeNode
        """
## code here
#1
"""
Wrong Answer
Input: [63,20,null,2,40,null,null,null,52,null,null], 63
Output: []
Expected: [63,20,null,2,40,null,null,null,52]

Success
Runtime: 72 ms, faster than 84.04% of Python3 online submissions for Search in a Binary Search Tree.
Memory Usage: 14.8 MB, less than 100.00% of Python3 online submissions for Search in a Binary Search Tree.
"""
class Solution:
    def searchBST(self, root, val):        
        if not root: return None
        if root.val == val: return root
        
        node_list = [[root]]
        checked = 0
        while checked != len(node_list):
            level = []
            for node in node_list[checked]:
                if node:
                    if node.left: level += [node.left]
                    if node.right: level += [node.right]
            if level: node_list += [level]
            for node in level:
                if node.val == val:
                    return node
            checked += 1
        return None


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