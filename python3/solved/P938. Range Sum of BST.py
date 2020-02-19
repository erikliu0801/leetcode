# ToDo:

"""
938. Range Sum of BST
Easy

Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example 1:
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23

Note:

    The number of nodes in the tree is at most 10000.
    The final answer is guaranteed to be less than 2^31.
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
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
## test part
class Solution:
    def rangeSumBST(self, root, L, R):
        """
        root: TreeNode
        L: int
        R: int
        rtype: int
        """

## code here
#1
"""
Success
Runtime: 304 ms, faster than 14.86% of Python3 online submissions for Range Sum of BST.
Memory Usage: 21 MB, less than 100.00% of Python3 online submissions for Range Sum of BST.
"""
class Solution:
    def rangeSumBST(self, root, L, R):

        def inorder(root):
            res = []
            if root:
                res.append(root.val)
                res += inorder(root.left)
                res += inorder(root.right)
            return res

        vals = inorder(root)
        return sum([val for val in vals if (val>=L) and (val<=R)])


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