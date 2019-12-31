#226
def invertTree(root):
	pass

#231
def isPowerOfTwo(n):
	if n%2 == 1 and n != 1:
		return False
	else:
		i = 0
		while 2**i <= n:
			if 2**i == n:
				return True
			i += 1
		return False

#235
def lowestCommonAncestor(root, p, q):
	pass

#263
def primeFactorization(num):
	prime = 2
	checked_primes = set({2})
	x = set(range(3,num+1,2))
	primes = set()
	while prime <= num:
		if num % prime == 0:
			primes.add(prime)
			while num % prime == 0:
				num = num // prime
		if len(x) != 0:
			prime = min(x)
			checked_primes.add(prime)
			x.remove(prime)
			x -= x.intersection(set(range(prime**2,num+1,prime)))
	return primes



def isUgly(num):
	def findPrimes(n):
		pass
	num = abs(num)
	num_primes = findPrimes(num)
	if num_primes - set({2,3,5}) == set({}):
		return True
	return False

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
	# input_nums = [[4, 2, 7, 1, 3, 6, 9]]
	# for nums in input_nums:
	# 	root = TreeNode(nums[0])
	# 	for i in nums[1:]:
	# 		root.insert(i)
	# invertTree(root)

	#231
	# print(isPowerOfTwo(16))

	#263
	import time
	now = time.time()
	for i in range(1, 2**31-1):
		print(primeFactorization(i))
	print(time.time() - now)