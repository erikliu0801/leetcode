# ToDo:

"""
606. Construct String from Binary Tree
Easy

You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.

Example 1:

Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".

Example 2:

Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.


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
    def tree2str(self, t: TreeNode) -> str:
        
## test part
def tree2str(t):
	"""
	t: TreeNode
	rtype: str:
	"""
## code here
#1
"""
[1,2,3,4]
"(1(2(4))(3))"
"""
def tree2str(t):
	res = ''
	if t:
		res = '(' + str(t.val) + tree2str(t.left) + tree2str(t.right) +')'
	return res

#1.1
"""
input: [1,2,3,null,4]
Output: "1(2(4))(3)"
Expected: "1(2()(4))(3)"

Success
Runtime: 52 ms, faster than 54.38% of Python3 online submissions for Construct String from Binary Tree.
Memory Usage: 14.8 MB, less than 91.67% of Python3 online submissions for Construct String from Binary Tree.
"""
def tree2str(t):
	def helper(t):
		res = ''
		if t:
			if not t.left and t.right:
				left = '()'
			else:
				left = helper(t.left)
			res = '(' + str(t.val) + left + helper(t.right) +')'
		return res
	return helper(t)[1:-1]



# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_list = [[1,2,3], [1,2,3,4], ]
	expected_output = ["1(2)(3)", "1(2(4))(3)"]
	for i in range(len(input1)):
		if func(input1[i]) != expected_output[i]:
			print("Wrong!!!")
			print(func(input1[i]))
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