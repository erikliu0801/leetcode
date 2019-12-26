# ToDo:

"""
203. Remove Linked List Elements
Easy

Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5



"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
	def removeElements(self, head: ListNode, val: int) -> ListNode:

## test part
def removeElements(head, val):
	"""
	head: ListNode
	val: int
	rtype: ListNode
	"""
## code here
#1
def removeElements(head, val):
	if head.val == val:
		if head.next == None:
			head = None
		else:
			head = head.next
	if head.next != None:
		removeElements(head.next, val)
	return head

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