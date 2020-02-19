# ToDo:

"""
965. Univalued Binary Tree
Easy

A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.

Note:

    The number of nodes in the given tree will be in the range [1, 100].
    Each node's value will be an integer in the range [0, 99].

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
    def isUnivalTree(self, root: TreeNode) -> bool:
        
## test part
class Solution:
    def isUnivalTree(self, root):
        """
        root: TreeNode
        rtype: bool
        """

## code here
#1
"""
Success
Runtime: 28 ms, faster than 72.81% of Python3 online submissions for Univalued Binary Tree.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Univalued Binary Tree.
"""
class Solution:
    def isUnivalTree(self, root):

        vals = set()

        def inorder(root):
            if root:
                vals.add(root.val)
                inorder(root.left)
                inorder(root.right)

        inorder(root)
        return len(vals) == 1

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