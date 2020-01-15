# ToDo:

"""
83. Remove Duplicates from Sorted List
Easy

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
## test part
def deleteDuplicates(head):
 	"""
 	head: ListNode
 	rtype: ListNode
 	"""
## code here
#1
"""
cannot control duplicates in the end
"""
def deleteDuplicates(head):
	new = ListNode(float('-inf'))
	new_head = new
	while head != None:
		if head.val != new.val:
			new.val = head.val
			if head.next != None:
				new.next = ListNode(head.val) #
			head, new = head.next, new.next
		else:
			head = head.next
	return new_head

#1.1
"""
[]
"""
def deleteDuplicates(head):
	new = ListNode(head.val)
	new_head = new
	while head != None:
		if head.val != new.val:
			new.next = ListNode(head.val)
			head, new = head.next, new.next
		else:
			head = head.next
	return new_head

#1.2
"""
Success
Runtime: 36 ms, faster than 94.91% of Python3 online submissions for Remove Duplicates from Sorted List.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Remove Duplicates from Sorted List.
"""
def deleteDuplicates(head):
	if type(head) == ListNode:
		new = ListNode(head.val)
		new_head = new
		while head != None:
			if head.val != new.val:
				new.next = ListNode(head.val)
				head, new = head.next, new.next
			else:
				head = head.next
		return new_head
	else:
		return 


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

	input_list = [
	[1,1,2],
	[1,1,2,3,3]]
	expected_output = [
	[1,2],
	[1,2,3]]

	# for i in range(len(input_list)):
	# 	if LinkedList2List(deleteDuplicates(List2LinkedList(input_list[i]))) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(LinkedList2List(deleteDuplicates(List2LinkedList(input_list[i]))))
	# 	else:
	# 		print("Right")
	print(LinkedList2List(deleteDuplicates(List2LinkedList(input_list[-1]))))
	

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