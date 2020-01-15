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

#507
def checkPerfectNumber(num):
	divisors = set([1])
	import math
	divisor = int(math.sqrt(num))
	while divisor != 1:
		if num%divisor == 0:
			divisors.add(divisor)
			divisors.add(num//divisor)
		divisor -= 1
	divisors.discard(num)
	return num == sum(divisors)

#509
def fib(N):
	if N < 1:
		return 0
	elif N == 1:
		return 1
	else:
		return fib(N-1) + fib(N-2)

if __name__ == "__main__":
	class TreeNode:
		def __init__(self, x):
			self.val = x
			self.left = None
			self.right = None

	#504
	# print(convertToBase7())

	#507
	# print(checkPerfectNumber(28))

	# for i in range(1,1000000000):
	# 	if checkPerfectNumber(i):
	# 		print(i)

	#509
	for i in range(1,31):
		print(fib(i))