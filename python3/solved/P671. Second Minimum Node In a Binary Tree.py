# ToDo:

"""
671. Second Minimum Node In a Binary Tree
Easy

Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:

Input: 
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.

 

Example 2:

Input: 
    2
   / \
  2   2

Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.

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
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        
## test part
class Solution:
    def findSecondMinimumValue(self, root):
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
Expected: 2

Success
Runtime: 28 ms, faster than 61.31% of Python3 online submissions for Second Minimum Node In a Binary Tree.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Second Minimum Node In a Binary Tree.
"""
class Solution:
    def findSecondMinimumValue(self, root):
        if not root: return -1
        vals = set()

        def inorder(root):
            if root:
                vals.add(root.val)
                inorder(root.left)
                inorder(root.right)

        inorder(root)
        vals.remove(min(vals))
        if vals: return min(vals)
        return -1

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