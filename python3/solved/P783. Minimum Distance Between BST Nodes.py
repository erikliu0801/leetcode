# ToDo:

"""
783. Minimum Distance Between BST Nodes
Easy

Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.

Note:

    The size of the BST will be between 2 and 100.
    The BST is always valid, each node's value is an integer, and each node's value is different.
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
    def minDiffInBST(self, root: TreeNode) -> int:
        
## test part
class Solution:
    def minDiffInBST(self, root):
        """
        root: TreeNode
        rtype: int
        """
## code here
#1
"""
Wrong Answer
Your input: [1,2]
Output: 1
Expected: -1

Success
Runtime: 24 ms, faster than 95.01% of Python3 online submissions for Minimum Distance Between BST Nodes.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Minimum Distance Between BST Nodes.
"""
class Solution:
    def minDiffInBST(self, root):
        if not root: return
        vals = list()

        def inorder(root):
            if root:
                vals.append(root.val)
                inorder(root.left)
                inorder(root.right)
        
        inorder(root)
        if len(vals) == 1: return
        vals.sort()
        res = float('inf')
        for i in range(len(vals)-1):
            res = min(res, abs(vals[i]-vals[i+1]))
        return res






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