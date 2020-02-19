# ToDo:

"""
872. Leaf-Similar Trees
Easy

Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.

Note:
    Both of the given trees will have between 1 and 100 nodes.
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
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
## test part
class Solution:
    def leafSimilar(self, root1, root2):
        """
        root1: TreeNode
        root2: TreeNode
        rtype: bool
        """
## code here
#1
"""
Wrong Answer
Your input:
[3,5,1,6,2,9,8,null,null,8,4]
[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
Output: true
Expected: false

Success
Runtime: 20 ms, faster than 99.52% of Python3 online submissions for Leaf-Similar Trees.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Leaf-Similar Trees.
"""
class Solution:
    def leafSimilar(self, root1, root2):

        def inorder(root):
            leaf = []
            if root:
                if root.left is None and root.right is None:
                    leaf.append(root.val)
                leaf += inorder(root.left)
                leaf += inorder(root.right)
            return leaf

        return inorder(root1) == inorder(root2)




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