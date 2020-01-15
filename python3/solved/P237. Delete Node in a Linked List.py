# ToDo:

"""
237. Delete Node in a Linked List
Easy

Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

Given linked list -- head = [4,5,1,9], which looks like following:

 

Example 1:

Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

Example 2:

Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.

 

Note:

	The linked list will have at least two elements.
	All of the nodes' values will be unique.
	The given node will not be the tail and it will always be a valid node of the linked list.
	Do not return anything from your function.



"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
	def deleteNode(self, node):
		"""
		:type node: ListNode
		:rtype: void Do not return anything, modify node in-place instead.
		"""

## test part
def deleteNode(self, node):
		"""
		:type node: ListNode
		:rtype: void Do not return anything, modify node in-place instead.
		"""
## code here
#1
"""
'head' referenced befor assignment
"""
def deleteNode(self, node):
	if head == node:
		head = head.next
	else:
		n0 = head
		n1 = head.next
		while n1 != node:
			n0 = n1
			n1 = n1.next	
		n0.next = n1.next

#1.1
"""
Success
Runtime: 36 ms, faster than 79.99% of Python3 online submissions for Delete Node in a Linked List.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Delete Node in a Linked List.
"""
def deleteNode(self, node):
	node.val = node.next.val
	node.next = node.next.next


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