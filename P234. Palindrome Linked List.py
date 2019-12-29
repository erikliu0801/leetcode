# ToDo:

"""
234. Palindrome Linked List
Easy
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

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
    def isPalindrome(self, head: ListNode) -> bool:
        
## test part
def isPalindrome(head):
	"""
	head: ListNode
	rtype: bool
	"""
## code here
#1
"""
adjust from P206 reverseList(head) X => pointer issue

Success
Runtime: 68 ms, faster than 86.67% of Python3 online submissions for Palindrome Linked List.
Memory Usage: 23 MB, less than 100.00% of Python3 online submissions for Palindrome Linked List.
"""
def isPalindrome(head):
	def LinkedList2List(ListNode):
		list1 = []
		l0 = ListNode
		while l0 != None:
			list1.append(l0.val)
			l0 = l0.next
		return list1
	nums = LinkedList2List(head)
    reverse_nums = nums[::-1]
	return nums == reverse_nums


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