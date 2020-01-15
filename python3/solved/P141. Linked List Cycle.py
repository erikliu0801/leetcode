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
	def pathLinkedList(head):
		linked_list = []
		while head != None or head in linked_list:
			linked_list.append(head)
			head = head.next
		return linked_list
	linked_list = pathLinkedList(head).reverse()
	for i, node in enumerate(linked_list):
		if node in linked_list[i+1:]:
			return True
	return False
#1.1
"""
Success
Runtime: 1204 ms, faster than 5.11% of Python3 online submissions for Linked List Cycle.
Memory Usage: 15.9 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.
"""
def hasCycle(head):
	linked_list = []
	while head != None:
		if head in linked_list:
			return True
		linked_list.append(head)
		head = head.next
	return False
	

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

	def LinkedList2List(ListNode):
		"""
		ListNode: Head
		rtype: List
		"""
		list1 = []
		l0 = ListNode
		while l0 != None:
			list1.append(l0.val)
			l0 = l0.next
		return list1
	
	def List2LinkedList(List):
		"""
		rtype: Head of ListNode
		"""
		l = ListNode(0)
		l0 = l
		for i in range(len(List)):
			l.val = List[i]
			if i + 1 != len(List):
				l.next = ListNode(0)
				l = l.next
		return l0
	
	input_linked_list = [[3,2,0,-4]]
	expected_output = [True]
	for i in range(len(input_linked_list)):
		if hasCycle(List2LinkedList(input_linked_list[i])) != expected_output[i]:
			print("Wrong!!!")
			print(hasCycle(List2LinkedList(input_linked_list[i])))
		else:
			print("Right")		
	# print(hasCycle(List2LinkedList(input_linked_list[-1])))

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