# ToDo:

"""
637. Average of Levels in Binary Tree
Easy
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.

Example 1:

Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

Note:

    The range of node's value is in the range of 32-bit signed integer.
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
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
## test part
class Solution:
    def averageOfLevels(self, root):
        """
        root: TreeNode
        rtype: List[float]
        """

## code here
#1
"""
Wrong Answer
Input: [3,1,5,0,2,4,6]
Output: [3.00000,3.00000,1.00000,5.00000]
Expected: [3.0,3.0,3.0]

Success
Runtime: 48 ms, faster than 79.44% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 15 MB, less than 100.00% of Python3 online submissions for Average of Levels in Binary Tree.
"""
class Solution:
    def averageOfLevels(self, root):
        def levelorder(root):
            if not root: return [], []            
            
            #
            node_list = [[root]]
            checked = 0
            while checked != len(node_list):
                level = []
                for node in node_list[checked]:
                    if node:                        
                        if node.left: level += [node.left]
                        if node.right: level += [node.right]
                if level: node_list += [level]
                checked += 1
            
            #
            vals_list = []
            for l in node_list:
                level = []
                for node in l:
                    level += [node.val]
                vals_list += [level]

            return vals_list

        res = []
        level_vals = levelorder(root)
        for l in level_vals:
            if l: res.append(sum(l)/len(l))

        return res

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input1 = [[3,9,20,15,7], [], [3,1,5,0,2,4,6]]
    expected_output = [[3.0, 14.5, 11.0], [], [3.0, 3.0, 3.0]]
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