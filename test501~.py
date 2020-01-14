#501
def findMode(root):
	pass

#504
def convertToBase7(num):
	negative = False
	if num < 0:
		negative = True
		num = abs(num)
	elif  num == 0:
		return '0'
	import math
	digits = int(math.log(num,7))
	sevenbasenum = ''
	while digits != -1:
		sevenbasenum = sevenbasenum + str(num//(7**digits))
		num = num % (7**digits)
		digits -= 1
	if negative:
		return '-' + sevenbasenum
	return sevenbasenum

if __name__ == "__main__":
	class TreeNode:
		def __init__(self, x):
			self.val = x
			self.left = None
			self.right = None

	#504
	print(convertToBase7())