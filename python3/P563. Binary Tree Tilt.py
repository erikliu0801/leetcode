# ToDo:

"""
563. Binary Tree Tilt
Easy

Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:

Input: 
         1
       /   \
      2     3
Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1

Note:

    The sum of node values in any subtree won't exceed the range of 32-bit integer.
    All the tilt values won't exceed the range of 32-bit integer.

Hint:
	1.Don't think too much, this is an easy problem. Take some small tree as an example.

	!!2.Can a parent node use the values of its child nodes? How will you implement it?

	3.May be recursion and tree traversal can help you in implementing.

	4.What about postorder traversal, using values of left and right childs?
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
    def findTilt(self, root: TreeNode) -> int:
        
## test part
class Solution:
    def findTilt(self, root):
        """
        root: TreeNode
        rtype: int
        """
## code here
#1
class Solution:
    def findTilt(self, root):
        
        def tilt(node):
            if not node:
                return 0
            
            l = node.left
            r = node.right
            if l == None and r == None: return 0
            elif l == None: return r.val
            elif r == None: return l.val
            else: return abs(r.val-l.val)
       
        if not root: return 0

        t = tilt(root)
        return sum([t, self.findTilt(root.left), self.findTilt(root.right)])

#1.1
"""
Wrong Answer
Input: [1,2,3,4,null,5]
Output: 10
Expected: 11
"""
class Solution:
    def findTilt(self, root):
                
        if not root: return 0
        
        l = root.left
        r = root.right
        if l == None and r == None: t = 0
        elif l == None: t = r.val
        elif r == None: t = l.val
        else: t =  abs(r.val-l.val)
       
        return sum([t, self.findTilt(root.left), self.findTilt(root.right)])

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