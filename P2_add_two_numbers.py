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
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

## test part
def addTwoNumbers(self, l1, l2):

## code here
# 1.1 Linked-List -> Int -> Linked-List => Accepted Runtime: 40 ms
"""
Memory Limit Exceeded
"""
class Solution:
	def addTwoNumbers(self, l1, l2):
		def LL2Int(Linked_List): #ok
			LL_Int = 0
			i = 0
			while Linked_List.next != None:
				LL_Int += Linked_List.val*10**i
				i += 1
				Linked_List = Linked_List.next
			LL_Int += Linked_List.val*10**i
			return LL_Int
		def Int2LL(Int): #bug
			i = 0
			var_list = [] # List of objects(ListNode)
			while Int//10 != 0:
				var_list.append(ListNode(0))
				var_list[i].val = Int%10
				if i != 0:
					var_list[i-1].next = var_list[i]
				i += 1
				Int = Int//10
			var_list.append(ListNode(0))
			var_list[i].val = Int%10
			var_list[i-1].next = var_list[i]
			return var_list
		return Int2LL(LL2Int(l1) + LL2Int(l2))[0]

# 1.2 Save Memory
class Solution:
	def addTwoNumbers(self, l1, l2):
		def LL2Int(Linked_List): #ok
			LL_Int = 0
			i = 0
			while Linked_List.next != None:
				LL_Int += Linked_List.val*10**i
				i += 1
				Linked_List = Linked_List.next
			LL_Int += Linked_List.val*10**i
			return LL_Int
			gc.enable()
		def Int2LL(Int): #bug
			i = 0
			var_list = [] # List of objects(ListNode)
			while Int//10 != 0:
				var_list.append(ListNode(0))
				var_list[i].val = Int%10
				if i != 0:
					var_list[i-1].next = var_list[i]
				i += 1
				Int = Int//10
			var_list.append(ListNode(0))
			var_list[i].val = Int%10
			var_list[i-1].next = var_list[i]
			return var_list
			gc.enable()
		return Int2LL(LL2Int(l1) + LL2Int(l2))[0]


# 2
	def addTwoNumbers(self, l1, l2):
		carry = 0
		l_sum = ListNode(0)
		while l1.next != None:
			l_sum = ListNode(0)
			l_sum.val = l1.val + l2.val + carry
			carry = l_sum.val%10
			return l_sum
			l_sum, l1, l2 = l_sum.next, l1.next, l2.next
		return l_sum
		
# 2.2
	def addTwoNumbers(self, l1, l2):
		l_sum = []		
		x, y = l1, l2
		carry = 0
		while x.next != "End":
			l_sum.append((x.val+y.val+carry)%10)
			carry = (x.val+y.val+carry)//10
			x, y = x.next, y.next
			if x.next == None:
				x.next = "End"
				la_sum = ListNode(l_sum[0])
		z = la_sum.next
		for i in len(l_sum)-1:
			z = ListNode(l_sum[i+1])
			z = z.next
		return la_sum

# 2.3
	def addTwoNumbers(self, l1, l2):
		l_sum = []		
		x, y = l1, l2
		carry = 0
		while x.val:
			l_sum.append((x.val+y.val+carry)%10)
			carry = (x.val+y.val+carry)//10
			x, y = x.next, y.next
		z = la_sum.next
		for i in len(l_sum)-1:
			z = ListNode(l_sum[i+1])
			z = z.next
		return la_sum


# 2.4
	def addTwoNumbers(self, l1, l2):
		l1_num = 0
		if 

# 3 List of Objects(ListNode)
	def addTwoNumbers(self, l1, l2):
		def list_LL(first_ListNode):
			var_list = [] # List of objects(ListNode)
			_ListNode = first_ListNode
			while _ListNode:
				var_list.append(_ListNode)
				_ListNode = _ListNode.next
			return var_list
		def twoListSum(List1,List2):
			ListSum = []
			for i in List1:
				ListSum.append(List1[i].val+List2[i].val)
			return ListSum
		


# Test
## Functional Test
"""
Condition:

"""
# l1 = (2 -> 4 -> 3)
# l2 = (5 -> 6 -> 4)
l10, l11, l12 = ListNode(2), ListNode(4), ListNode(3)
l10.next, l11.next= l11, l12
l20, l21, l22 = ListNode(5), ListNode(6), ListNode(4)
l20.next, l21.next= l21, l22

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