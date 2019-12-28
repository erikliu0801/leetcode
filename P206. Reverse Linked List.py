# ToDo:

"""
206. Reverse Linked List
Easy
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

## test part
def reverseList(head):
	"""
	head: ListNode
	rtype: ListNode
	"""
## code here
#1
def reverseList(head):
	n1, n2, n3 = head, head.next, head.next.next
	n2.next = n1
	n3.next = n2

#1.1
"""
Runtime Error
[1,2]
"""
def reverseList(head):
	if type(head) != ListNode:
		return
	elif head.next == None:
		return head
	else:
		node = head.next #n2
		head.next = None #n1->X
		while node:
			new_head = node.next #n3
			node.next = head #n2->n1
			if new_head.next != None:
				head = node # n1 = n2
				node = new_head # n2 = n3
			else:
				new_head.next = node #n3->n2
				return new_head

#1.2
"""
Success
Runtime: 36 ms, faster than 72.24% of Python3 online submissions for Reverse Linked List.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Reverse Linked List.
"""
def reverseList(head):
	if type(head) != ListNode:
		return
	elif head.next == None:
		return head
	else:
		node = head.next #n2
		head.next = None #n1->X
		while node.next: #if n3 exist
			new_head = node.next #n3
			node.next = head #n2->n1
			if new_head.next != None:
				head = node # n1 = n2
				node = new_head # n2 = n3
			else:
				new_head.next = node #n3->n2
				return new_head
		node.next = head
		return node
		

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