#83
def deleteDuplicates(head):
	new = ListNode(head.val)
	new_head = new
	while head != None:
		if head.val != new.val:
			new.next = ListNode(head.val)
			head, new = head.next, new.next
		else:
			head = head.next
	return new_head

if __name__ == '__main__':
	#83
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

	input_list = [
	[1,1,2],
	[1,1,2,3,3],
	[],
	[1],
	[1,1]]
	expected_output = [
	[1,2],
	[1,2,3],
	[],
	[1],
	[1]]

	for i in range(len(input_list)):
		if LinkedList2List(deleteDuplicates(List2LinkedList(input_list[i]))) != expected_output[i]:
			print("Wrong!!!")
			print(LinkedList2List(deleteDuplicates(List2LinkedList(input_list[i]))))
		else:
			print("Right")
	# print(LinkedList2List(deleteDuplicates(List2LinkedList(input_list[-1]))))