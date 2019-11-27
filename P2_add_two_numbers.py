# ToDo:


"""
2. Add Two Numbers: Linked List, Math
Medium

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Concepts
## Problem breakup
"""
1st Node: Digits -> 2.Node
	if 1.Node > 10 -> 2.Node + 1
2nd Node: Tens Digit -> 3.Node
	if 2.Node > 10 -> 3.Node + 1
3rd Node: Hundreds Digit

"""

## Linked List
"""
pointer to next node(not previous one) -> one way link

class ListNode:
  def __init__(self, data): 
    # store data
    self.data = data
    # store the reference (next item)
    self.next = None
    return

class SingleLinkedList:
  def __init__(self): 
    self.head = None
    self.tail = None
    return

def add_list_item(self, item):
  # make sure item is a proper node  
  if not isinstance(item, ListNode):
    item = ListNode(item)
    
  if self.head is None:
    self.head = item
  else:
    self.tail.next = item
    
  self.tail = item
  return
"""


# Code
## submit part

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

## test part
def addTwoNumbers(self, l1, l2):

## code here
# 1
def addTwoNumbers(self, l1, l2):



# Test
## Functional Test
"""
Condition:

"""


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