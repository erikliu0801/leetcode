# ToDo:

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

# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	input = []
	expected_output = []
	for i, j in enumerate(input):
		if func(input[i]) != expected_output[i]:
			print("Wrong!!!")
			print(func(input[i]))
		else:
			print("Right")		
	# print(func(input[-1]))
	

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