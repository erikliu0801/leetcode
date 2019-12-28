#226
def invertTree(root):
	pass

if __name__ == '__main__':
	class TreeNode:
		def __init__(self, x):
			self.val = x
			self.left = None
			self.right = None
   
		def PrintTree(self):
			if self.left:
				self.left.PrintTree()
			print(self.val),
			if self.right:
				self.right.PrintTree()

		def insert(self, val):
			if self.val:
				if val < self.val :
					if self.left is None:
						self.left = TreeNode(val)
					else:
						self.left.insert(val)
				elif val > self.val:
					if self.right is None:
						self.right = TreeNode(val)
					else:
						self.right.insert(val)
			else:
				self.val = val

	#226
	input_nums = [[4, 2, 7, 1, 3, 6, 9]]
	for nums in input_nums:
		root = TreeNode(nums[0])
		for i in nums[1:]:
			root.insert(i)
	invertTree(root)