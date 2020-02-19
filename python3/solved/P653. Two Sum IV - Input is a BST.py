# ToDo:

"""
653. Two Sum IV - Input is a BST
Easy

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: [5,3,6,2,4,null,7]
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9
Output: True

Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28
Output: False
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
    def findTarget(self, root: TreeNode, k: int) -> bool:
        
## test part
class Solution:
    def findTarget(self, root, k):
        """
        root: TreeNode
        k: int
        rtype: bool
        """
## code here
#1
"""
Wrong Answer
Input: [1,0,4,-2,null,3], 7
Output: false
Expected: true

Success
Runtime: 96 ms, faster than 22.45% of Python3 online submissions for Two Sum IV - Input is a BST.
Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Two Sum IV - Input is a BST.
"""
class Solution:
    def findTarget(self, root, k):
        def inOrderTraversal(root):
            res = []
            if root:
                res = inOrderTraversal(root.left)
                res.append(root.val)
                res = res + inOrderTraversal(root.right)
            return res
        vals = inOrderTraversal(root)
        vals.sort()
        for i, val in enumerate(vals[:-1]):
            if k-val in vals[i+1:]: return True
            if k-val < val: break
        return False



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