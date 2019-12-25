#141
def hasCycle(head):
	linked_list = []
	while head != None:
		if head in linked_list:
			return True
		linked_list.append(head)
		head = head.next
	return False

#168
def convertToTitle(n):	
	if n <= 0:
		return
	else:
		digits = ['Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y']	
		digits_sum, digits_num, digits_level = 0, 1, 0
		while digits_sum < n:
			digits_num *= 26
			digits_level += 1
			digits_sum += digits_num
		if digits_sum == n:
			return 'Z' * digits_level
		else:
			all_digits = ''
			while digits_level > 0:
				all_digits = digits[n % 26] + all_digits
				if n % 26 == 0:
					n = n//26 -1
				else:
					n = n//26
				digits_level -= 1
			return all_digits

#169
def majorityElement(nums):
	for num in set(nums):
		if nums.count(num) > len(nums)//2:
			return num

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
	# input_linked_list = [[3,2,0,-4]]
	# expected_output = [True]
	# for i in range(len(input_linked_list)):
	# 	if hasCycle(List2LinkedList(input_linked_list[i])) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(hasCycle(List2LinkedList(input_linked_list[i])))
	# 	else:
	# 		print("Right")		
	# print(hasCycle(List2LinkedList(input_linked_list[-1])))

	#168
	# for i in range(1,28):
	# 	print(convertToTitle(i))
	# input_int = [1, 26, 28, 701, 702, 703, 17576, 18278, 18279]
	# expected_output = ['A', 'Z', 'AB', 'ZY', 'ZZ', 'AAA', 'YYZ', 'ZZZ', 'AAAA']
	# for i in range(len(input_int)):
	# 	if convertToTitle(input_int[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(convertToTitle(input_int[i]))
	# 	else:
	# 		print("Right")
	# print(convertToTitle(182789))

	#169
	print(majorityElement([2,2,1,1,1,2,2]))