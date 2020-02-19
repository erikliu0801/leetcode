# ToDo:

"""
572. Subtree of Another Tree
Easy

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Hint:
    1.Which approach is better here- recursive or iterative?

    2.If recursive approach is better, can you write recursive function with its parameters?

    3.Two trees s and t are said to be identical if their root values are same and their left and right subtrees are identical. Can you write this in form of recursive formulae?

    4.Recursive formulae can be: isIdentical(s,t)= s.val==t.val AND isIdentical(s.left,t.left) AND isIdentical(s.right,t.right)

"""
# Conditions & Concepts
"""
t is the subtree of s
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
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
## test part
class Solution:
    def isSubtree(self, s, t):
        """
        s: TreeNode
        t: TreeNode
        rtype: bool
        """
## code here
#1
# class Solution:
#     def isSubtree(self, s, t):
#         def inorder(root):
#             res = []
#             if not root: return [None]
#             res.append(root.val)
#             res += inorder(root.left)
#             res += inorder(root.right)
#             return res
        
#         if not s and not t: return True
#         if not s or not t: return False
        
#         res_l, res_r = False, False
#         if s.left: res_l = self.isSubtree(s.left, t)
#         if s.right: res_r = self.isSubtree(s.right, t)
        
#         return (inorder(t) in inorder(s)) or res_l or res_r


#2
class Solution:
    def isSubtree(self, s, t):
        if not s and not t: return True
        if not t: return False
        t_val = t.val

        def isIdentical(root1, root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            if root1.left != root2.left or root1.right != root2.right: return False
            return True and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)

        def inordersearch(root, val):
            if not root: return False
            if root.val == val: return root
            l = inordersearch(root.left, val)
            if l: return l
            r = inordersearch(root.right, val)            
            if r: return r

        while inordersearch(s, t_val):
            if isIdentical()


#2.1
class Solution:
    def isSubtree(self, s, t):
        if not s and not t: return True
        if not t: return False
        t_val = t.val

        def isIdentical(root1, root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            if root1.left != root2.left or root1.right != root2.right: return False
            return True and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)

        def inordersearch(root, val):
            res = []
            if root:  
                if root.val == val: 
                    res.append(root)
                    res += inordersearch(root.left, val)
                    res += inordersearch(root.right, val)
            return res

        p_nums = inordersearch(s, t_val)
        for p in p_nums:
            if isIdentical(t,p): return True
        return False

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
    input_s = [[3,4,5,1,2], [3,4,5,1,2,None,None,None,None,0], [3,4,5,1,2]]
    input_t = [[4,1,2], [4,1,2], [3,4,5]]
    expected_output = [True, False, False]
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