# ToDo:
# optimize test
"""
21. Merge Two Sorted Lists
Easy

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

"""
# Concepts


# Code
## submit part
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
## test part

## code here
#1
def mergeTwoLists(l1, l2):
	def LinkedList2List(ListNode):
		list1 = []
		l0 = ListNode
		while l0.next !=None:
			list1.append(l0.val)
			l0 = l0.next
	def List2LinkedList(List):
		for i, j in enumerate(List):
			name_list = []
			name = "l" + str(i)
			name_list.append(name)
			name_list[i].ListNode(j)
		return l0

	l1, l2 = LinkedList2List(l1), LinkedList2List(l2)
	list2 = []
	while l1 != [] or l2 != []:
		if l1[0]>l2[0]:
			list2.append(l2[0])
			l2 = l2[1:]
		else:
			list2.append(l1[0])
			l1 = l1[1:]
	list2 = list2 + l1 +l2

	for i, j in enumerate(list2):
			name_list = []
			name = "l" + i
			name_list.append(name)
			name_list[i].ListNode(j)
	
	return l0

#2
"""
Success
Runtime: 32 ms, faster than 93.21% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Merge Two Sorted Lists.
"""
def mergeTwoLists(l1, l2):
	if l1 or l2:
		l0 = ListNode(0)
		l = []
		while l1 and l2:
			if l1.val < l2.val:
				l0.val = l1.val
				l1 = l1.next
			else:
				l0.val = l2.val
				l2 = l2.next
			l.append(l0)
			l0.next = ListNode(0)
			l0 = l0.next	
		while l1:
			l0.val = l1.val
			l1 = l1.next
			l.append(l0)
			l0.next = ListNode(0)
			l0 = l0.next
		while l2:
			l0.val = l2.val
			l2 = l2.next
			l.append(l0)
			l0.next = ListNode(0)
			l0 = l0.next
		l[-1].next = None
		return l[0]
	else:
		if l1:
			return l1
		elif l2:
			return l2
		else:
			return


# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	class ListNode:
	    def __init__(self, x):
	        self.val = x
	        self.next = None
	class LinkedListFuc:
		def LinkedList2List(ListNode):
			list1 = []
			l0 = ListNode
			while l0.next !=None:
				list1.append(l0.val)
				l0 = l0.next
			list1.append(l0.val)
			return list1
		def List2LinkedList(List):
			l = [] 
			l0 = ListNode(List[0])
			for i, j in enumerate(List):
				l0.val = j
				if i + 1 < len(List):
					l0.next = ListNode(List[i+1])
				l.append(l0)
				if i + 1 < len(List):
					l0 = l0.next
			return l
	input0 = [[1,2,4],[1,3,4]]
	input1 = [[[1,2,4],[1,3,4]]]
	expected_output = [[1,1,2,3,4,4]]
	# print(LinkedListFuc.List2LinkedList(input0[0]))
	# print(LinkedListFuc.List2LinkedList(input0[0])[2].val)
	
	for i, j in enumerate(input1):
		l1, l2 = LinkedListFuc.List2LinkedList(input1[i][0]), LinkedListFuc.List2LinkedList(input1[i][1])
		if LinkedListFuc.LinkedList2List(mergeTwoLists(l1[0], l2[0])) != expected_output[i]:
			print("Wrong!!! Output:", LinkedListFuc.LinkedList2List(mergeTwoLists(l1[0], l2[0])))
			print("Expected Output:", expected_output[i])
		else:
			print("Right")
	

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