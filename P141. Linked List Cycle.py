# ToDo:

"""
141. Linked List Cycle
Easy

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

 

Follow up:

Can you solve it using O(1) (i.e. constant) memory?


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
	def hasCycle(self, head: ListNode) -> bool:

## test part
def hasCycle(head):
	"""
	head: ListNode
	rtype: bool
	"""
## code here
#1
def hasCycle(head):

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	class ListNode:
		def __init__(self, x):
			self.val = x
			self.next = None
	input1 = []
	expected_output = []
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