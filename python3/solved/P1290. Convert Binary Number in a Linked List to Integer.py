# ToDo:

"""
1290. Convert Binary Number in a Linked List to Integer
Easy

Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

Constraints:

    The Linked List is not empty.
    Number of nodes will not exceed 30.
    Each node's value is either 0 or 1.


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
    def getDecimalValue(self, head: ListNode) -> int:
        
## test part
def getDecimalValue(head):
	"""
	head: ListNode
	rtype: int
	"""

## code here
#1
"""
Success
Runtime: 16 ms, faster than 99.59% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Convert Binary Number in a Linked List to Integer.
"""
def getDecimalValue(head):
	s = ''
	while head:
		s += str(head.val)
		head = head.next
	return int(s, base=2)

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