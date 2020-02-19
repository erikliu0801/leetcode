# ToDo:

"""
617. Merge Two Binary Trees
Easy

Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:

Input: 
    Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
         3
        / \
       4   5
      / \   \ 
     5   4   7

Note: The merging process must start from the root nodes of both trees.
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
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
## test part

class Solution:
    def mergeTrees(self, t1, t2):
        """
        t1: TreeNode
        t2: TreeNode
        rtype: TreeNode
        """
## code here
#1
"""
t1 = t2; t1, t2 = t2, t1
    Wrong Answer
    Your input
    [1,3,2,5]
    [2,1,3,null,4,null,7]
    Output
    [3,4,5,5]
    Expected
    [3,4,5,5,4,null,7]

"""
class Solution:
    def mergeTrees(self, t1, t2):
        if not t1 and t2: #
            t1 = t2

        if t1 and t2:
            t1.val += t2.val       
            self.mergeTrees(t1.left, t2.left)
            self.mergeTrees(t1.right, t2.right)
        return t1

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