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

#88
def merge(nums1, m, nums2, n):
	nums2, i = nums2[:n], 0
	temp_num = nums1[0]
	for i in range(len(nums1)-m):
		nums1[-1-i] = 0
	while nums2 != []:
		if nums1[i] >= nums2[0] or nums1[i] == 0:
			nums1.insert(i, nums2[0])
			nums1.pop(-1)
			nums2.pop(0)
		elif len(nums1) - 1 == i and nums1[i] < nums2[0]:
			break
		i +=1
	return nums1

#100
def isSameTree(p, q):
	def levelOrderTraversal(TreeNode):
		"""
		rtype: left_list, right_list
		highest_treenode belongs to left_list
		"""
		level_order_treenode_left = [TreeNode]
		level_order_treenode_right = []
		m, n, last_len = 0, 0, 0
		while last_len != len(level_order_treenode_left + level_order_treenode_right):
			last_len, l, r = len(level_order_treenode_left + level_order_treenode_right), m, n
			level_order_treenode = level_order_treenode_left[m:] + level_order_treenode_right[n:]
			for i in range(len(level_order_treenode)):
				if level_order_treenode[i].left != None:
					level_order_treenode_left.append(level_order_treenode[i].left)
				else:
					level_order_treenode_left.append(None)
				if level_order_treenode[i].right != None:
					level_order_treenode_right.append(level_order_treenode[i].right)
				else:
					level_order_treenode_right.append(None)
				if level_order_treenode[i] in level_order_treenode_left:
					m += 1
				else:
					n += 1
		return level_order_treenode_left, level_order_treenode_right

	if p is None or q is None:
		if p is None and q is None:
			return True
		else:
			return False
	else:
		p_list_left, p_list_right = levelOrderTraversal(p)
		q_list_left, q_list_right = levelOrderTraversal(q)
		if len(p_list_left) != len(q_list_left) or len(p_list_right) != len(q_list_right):
			return False
		p_list, q_list = p_list_left + p_list_right, q_list_left + q_list_right
		for i in range(len(p_list)):
			if p_list[i].val != q_list[i].val:
				return False
		return True


if __name__ == '__main__':
	#83
	# class ListNode:
	# 	def __init__(self, x):
	# 		self.val = x
	# 		self.next = None
	# def LinkedList2List(ListNode):
	# 	"""
	# 	ListNode: Head
	# 	rtype: List
	# 	"""
	# 	list1 = []
	# 	l0 = ListNode
	# 	while l0 != None:
	# 		list1.append(l0.val)
	# 		l0 = l0.next
	# 	return list1
	# def List2LinkedList(List):
	# 	"""
	# 	rtype: Head of ListNode
	# 	"""
	# 	l = ListNode(0)
	# 	l0 = l
	# 	for i in range(len(List)):
	# 		l.val = List[i]
	# 		if i + 1 != len(List):
	# 			l.next = ListNode(0)
	# 			l = l.next
	# 	return l0
	#
	# input_list = [
	# [1,1,2],
	# [1,1,2,3,3],
	# [],
	# [1],
	# [1,1]]
	# expected_output = [
	# [1,2],
	# [1,2,3],
	# [],
	# [1],
	# [1]]
	#
	# for i in range(len(input_list)):
	# 	if LinkedList2List(deleteDuplicates(List2LinkedList(input_list[i]))) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(LinkedList2List(deleteDuplicates(List2LinkedList(input_list[i]))))
	# 	else:
	# 		print("Right")
	# print(LinkedList2List(deleteDuplicates(List2LinkedList(input_list[-1]))))

	#88
	input_nums1 = [
	[[1,2,3,0,0,0], 3],
	[[1,2,3,7,0,0], 3],
	[[1,2,3,7,0,0], 2],
	[[1,2,3,4,0,0,0],4],
	[[1,2,3,0,0,0], 2]
	]
	input_nums2 = [
	[[2,5,6], 3],
	[[2,5,6], 3],
	[[2,5,6,8], 4],
	[[2,5,6],2],
	[[2,5,6], 3]
	]
	expected_output = [
	[1,2,2,3,5,6],
	[1,2,2,3,5,6],
	[1,2,2,5,6,8],
	[1,2,2,3,4,5,0],
	[1,2,2,5,6,0]]

	for i in range(len(input_nums1)):
		if merge(input_nums1[i][0],input_nums1[i][1],input_nums2[i][0],input_nums2[i][1]) != expected_output[i]:
			print("Wrong!!!")
			print(merge(input_nums1[i][0],input_nums1[i][1],input_nums2[i][0],input_nums2[i][1]))
		else:
			print("Right")
	# print(merge(input_nums1[-1][0],input_nums1[-1][1],input_nums2[-1][0],input_nums1[-1][1]))