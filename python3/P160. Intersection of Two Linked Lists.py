# ToDo:

"""
160. Intersection of Two Linked Lists
Easy

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:

begin to intersect at node c1.

 

Example 1:

Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

 

Example 2:

Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

 

Example 3:

Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.

 

Notes:

    If the two linked lists have no intersection at all, return null.
    The linked lists must retain their original structure after the function returns.
    You may assume there are no cycles anywhere in the entire linked structure.
    Your code should preferably run in O(n) time and use only O(1) memory.



"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
## test part
def getIntersectionNode(headA, headB):
	"""
	headA: ListNode
	headB: ListNode
	rtype: ListNode
	"""
## code here
#1
"""
Time Limit Exceeded
"""
def getIntersectionNode(headA, headB):
	linked_list_A = []
	while headA != None:
		linked_list_A.append(headA)
		headA = headA.next
	while headB != None:
		if headB in linked_list_A:
			return headB
		else:
			headB = headB.next
	return 

#2 new
def getIntersectionNode(headA, headB):
	


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