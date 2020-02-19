# ToDo:

"""
590. N-ary Tree Postorder Traversal
Easy

Given an n-ary tree, return the postorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Follow up:

Recursive solution is trivial, could you do it iteratively?

Constraints:

    The height of the n-ary tree is less than or equal to 1000
    The total number of nodes is between [0, 10^4]

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        
## test part
class Solution:
    def postorder(self, root):
        """
        root: 'Node') -> List[int]
        """
## code here
#1
"""
Success
Runtime: 56 ms, faster than 30.28% of Python3 online submissions for N-ary Tree Postorder Traversal.
Memory Usage: 14.7 MB, less than 100.00% of Python3 online submissions for N-ary Tree Postorder Traversal.
"""
class Solution:
    def postorder(self, root):
        res = []
        if root:
            for child in root.children:
                res += self.postorder(child)
            res.append(root.val)
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