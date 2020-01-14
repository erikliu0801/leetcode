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
			return head
		else:
			head = head.next
	if head.next != None:
		removeElements(head.next, val)
	return head

#1.1
"""
[1,1]
2
"""
def removeElements(head, val):
	if type(head) != ListNode:
		return
	while head.val != val:
		if head.next != None:
			head = head.next
		else:
			return
	if head.next == None:
		return head
	else:
		l0, l1 = head, head
	while l1.next:
		if l1.next.val == val:
			l1.next = l1.next.next
		l1 = l1.next
	return l0

#1.2
"""
Wrong Answer
Input: [1,2,2,1] 2
Output: [1,2,1]
Expected: [1,1]
"""
def removeElements(head, val):
	if type(head) != ListNode:
		return
	while head.val == val:
		if head.next != None:
			head = head.next
		else:
			return
	if head.next == None:
		return head
	else:
		l0, l1 = head, head
	while l1.next:
		if l1.next.val == val:
			l1.next = l1.next.next
		if l1.next != None:
			l1 = l1.next
		else:
			break
	return l0

#1.3
"""
Success
Runtime: 68 ms, faster than 77.85% of Python3 online submissions for Remove Linked List Elements.
Memory Usage: 21.9 MB, less than 5.55% of Python3 online submissions for Remove Linked List Elements.
"""
def removeElements(head, val):
	if type(head) != ListNode:
		return
	while head.val == val:
		if head.next != None:
			head = head.next
		else:
			return
	if head.next == None:
		return head
	l1 = removeElements(head.next, val)
	if l1:
		head.next = l1
	else:
		head.next = None
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

	print(LinkedList2List(removeElements(List2LinkedList([1,2,6,3,4,5,6]),6)))
	print(LinkedList2List(removeElements(List2LinkedList([1,1]),2)))
	

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