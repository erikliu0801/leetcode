# ToDo:

"""
876. Middle of the Linked List
Easy

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
## test part
def middleNode(head):
	"""
	head: ListNode
	rtype: ListNode
	"""
## code here
#1
"""
Success
Runtime: 28 ms, faster than 60.12% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Middle of the Linked List.
"""
def middleNode(head):
	nodes = []
	while head:
		nodes.append(head)
		head = head.next
	return nodes[len(nodes)//2]

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