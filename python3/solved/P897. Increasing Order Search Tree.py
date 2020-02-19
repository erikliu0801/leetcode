# ToDo:

"""
897. Increasing Order Search Tree
Easy

Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9

Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  

Note:

    The number of nodes in the given tree will be between 1 and 100.
    Each node will have a unique integer value from 0 to 1000.



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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
## test part
class Solution:
    def increasingBST(self, root):
        """
        root: TreeNode
        rtype: TreeNode
        """
        
## code here
#1
"""
Success
Runtime: 100 ms, faster than 51.05% of Python3 online submissions for Increasing Order Search Tree.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Increasing Order Search Tree.
"""
class Solution:
    def increasingBST(self, root):
        if not root: return

        def inorder(root):
            res = []
            if root:
                res = inorder(root.left)
                res.append(root.val)
                res += inorder(root.right)
            return res

        vals = inorder(root)
        n0 = TreeNode(vals[0])
        n = n0

        for val in vals[1:]:
            n.right = TreeNode(val)
            n = n.right

        return n0

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