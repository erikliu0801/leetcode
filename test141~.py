#141
def hasCycle(head):
	linked_list = []
	while head != None:
		if head in linked_list:
			return True
			break
		linked_list.append(head)
		head = head.next
	return False


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

	#141
	input_linked_list = [[3,2,0,-4]]
	expected_output = [True]
	for i in range(len(input_linked_list)):
		if hasCycle(List2LinkedList(input_linked_list[i])) != expected_output[i]:
			print("Wrong!!!")
			print(hasCycle(List2LinkedList(input_linked_list[i])))
		else:
			print("Right")		
	# print(hasCycle(List2LinkedList(input_linked_list[-1])))
