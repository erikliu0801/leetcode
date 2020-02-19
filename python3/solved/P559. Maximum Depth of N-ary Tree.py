# ToDo:

"""
559. Maximum Depth of N-ary Tree
Easy

Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Constraints:

    The depth of the n-ary tree is less than or equal to 1000.
    The total number of nodes is between [0, 10^4].
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
        self.children = children #list
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
## test part
def maxDepth(root):
	"""
	root: 'Node'
	rtype: int
	"""
## code here
#1
def maxDepth(root):
	if not root:
		return 0
	#return max(maxDepth(root.left), maxDepth(root.right))+1 #children

	#return max(maxDepth(root.children))+1 
	#AttributeError: 'List' object has no attribute 'children'

	#return max(maxDepth(child) for child in root.children)+1 #ValueError: max() arg is an empty sequence

	#return root.count(None)
	#AttributeError: 'Node' object has no attribute 'count'

#1.1
"""
Success
Runtime: 48 ms, faster than 39.86% of Python3 online submissions for Maximum Depth of N-ary Tree.
Memory Usage: 14.6 MB, less than 100.00% of Python3 online submissions for Maximum Depth of N-ary Tree.
"""
def maxDepth(root):
	if not root:
		return 0
	depth = 0
	for child in root.children:
		depth = max(depth, maxDepth(child))
	return depth+1	

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