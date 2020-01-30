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

#290
def wordPattern(patternstr, str):
	nums_str = str.split(' ')
	if len(patternstr) != len(nums_str):
		return False
	p_to_s = {}
	have_ds = set()
	for dp, ds in zip(patternstr, nums_str):
		if dp not in p_to_s:
			if ds in have_ds:
				return False
			p_to_s[dp] = ds
			have_ds.add(ds)
		if p_to_s[dp] != ds:
			return False
	return True

#299
def getHint(secret, guess):
	if guess == '':
		return '0A0B'
	elif secret == guess:
		return str(len(secret)) + 'A0B'
	bulls, cows = 0, 0
	secret, guess = list(secret), list(guess)
	s_g_nums = list()
	for s_g in zip(secret,guess):
		s_g_nums.append(s_g)
	secret, guess = list(), list()
	for s_num, g_num in s_g_nums.copy():
		if s_num == g_num:
			bulls +=1
			s_g_nums.remove((s_num,g_num))
		else:
			secret.append(s_num)
			guess.append(g_num)
	for num in guess:
		if num in secret:
			cows += 1
			secret.remove(num)
	return str(bulls) + 'A' + str(cows) + 'B'

def isUgly(num):
	def findPrimes(n):
		pass
	num = abs(num)
	num_primes = findPrimes(num)
	if num_primes - set({2,3,5}) == set({}):
		return True
	return False

#392
def isSubsequence(s, t):
	i = 0
	for alphabet in t:
		if alphabet == s[i]:
			i += 1
		if i == len(s):
			break
	return i == len(s)

#405
def toHex(num):
	if num == 0:
		return "0"
	if num < 0:
		num += 4294967296
	import math
	hex_list = [str(x) for x in range(10)]
	hex_list.extend([chr(x) for x in range(97,103)])
	power = int(math.log(num,16))
	hex_num = ""
	while power >= 0:
		hex_num += hex_list[num // (16 ** power)]
		num %= (16 ** power)
		power -= 1
	return hex_num

def main():
	input_num = [16, 26, 0, -1, -2, -16]
	expected_output = ["10", "1a", "0", "ffffffff", "fffffffe", "fffffff0"]
	for i in range(len(input_num)):
		if toHex(input_num[i]) != expected_output[i]:
			print("Wrong!!!")
			print(toHex(input_num[i]))
		else:
			print("Right")
	# print(toHex(input_num[3]))

#409
def longestPalindrome(s):
	count_nums = list()
	for alphabet in set(s):
		count_nums.append(s.count(alphabet))
	longest_palindrome = 0
	for i, num in enumerate(count_nums):
		if num//2 >= 1:
			longest_palindrome += num - num%2
			count_nums[i] = num%2
	if 1 in count_nums:
		longest_palindrome += 1
	return longest_palindrome

#443
def compress(chars):
	alph = chars[0]
	start = 0
	alph_count_nums = list()
	for i, j in enumerate(chars):
		if i == len(chars)-1:
			if j != alph:
				alph_count_nums.append((alph, i-start))
				alph_count_nums.append((j, 1))
			else:
				alph_count_nums.append((alph, i-start+1))
		elif j != alph:
			alph_count_nums.append((alph, i-start))
			alph = j
			start = i
	#
	i = 0
	for alph, count in alph_count_nums:
		chars[i] = alph
		i += 1
		if count != 1:
			for c in list(str(count)):
				chars[i] = c
				i += 1
	for _ in range(len(chars)-i):
		chars.pop()
	#
	return chars

#459
def repeatedSubstringPattern(s):
	substring_nums = list()
	while s != str():
		substring_nums.append(s[:s.index(s[-1])+1])
		s = s[s.index(s[-1])+1:]
	substring_i = substring_nums.index(substring_nums[-1]) +1
	if substring_i == len(substring_nums) or len(substring_nums) % substring_i != 0:
		return False

	for i, substring in enumerate(substring_nums):
		if substring != substring_nums[i % substring_i]:
			return False

	return True

#476
def findComplement(num):
	num  = list(str(bin(num))[2:])
	complement = str()
	for j in num:
		if j == '1':
			complement = complement + '0'
		else:
			complement = complement + '1'
	return int(complement,2)

#482
def licenseKeyFormatting(S, K):
	S = list(S.upper())[::-1]
	key = str()
	key_part = str()
	for alph in S:
		if alph != '-':
			if len(key_part) < K:
				key_part = alph + key_part
			else:
				key = key_part + '-' + key
				key_part = alph
	if key_part != str() and key != str():
		return key_part + '-' + key[:-1]
	elif key_part != str() and key == str():
		return key_part
	return key[:-1]

#496
def nextGreaterElement(nums1, nums2):
	for i, num in enumerate(nums1):
		nums2_temp = nums2[nums2.index(num)+1:]
		if nums2_temp == list():
			nums1[i] = -1
		else:
			for num2 in nums2_temp:
				if num2 > num:
					nums1[i] = num2
					break
			if nums1[i] == num:
				nums1[i] = -1
	return nums1

#500
def findWords(words):
	row1 = set(['q','w','e','r','t','y','u','i','o','p'])
	row2 = set(['a','s','d','f','g','h','j','k','l'])
	row3 = set(['z','x','c','v','b','n','m'])
	for word in words.copy():
		word_tmp = set(word.lower())
		# if word_tmp not in row1 and word_tmp not in row2 and word_tmp not in row3:
		if word_tmp.issubset(row1) or word_tmp.issubset(row2) or word_tmp.issubset(row3):
			continue
		else:
			words.remove(word)
	return words

if __name__ == '__main__':
	main()
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
	# import time
	# now = time.time()
	# for i in range(1, 2**31-1):
	# 	print(primeFactorization(i))
	# print(time.time() - now)

	#290
	# input_patternstr = ["abba", "abba", "aaaa", "abba"]
	# input_str = ["dog cat cat dog", "dog cat cat fish", "dog cat cat dog", "dog dog dog dog"]
	# expected_output = [True, False, False, False]
	# for i in range(len(input_patternstr)):
	# 	if wordPattern(input_patternstr[i], input_str[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(wordPattern(input_patternstr[i], input_str[i]))
	# 	else:
	# 		print("Right")
	# print(wordPattern(input_patternstr[2], input_str[1]))

	#299
	# input_secret = ["1807", "1123", "11"]
	# input_guess = ["7810", "0111", "11"]
	# expected_output = ["1A3B", "1A1B", "2A0B"]
	# for i in range(len(input_secret)):
	# 	if getHint(input_secret[i], input_guess[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(getHint(input_secret[i], input_guess[i]))
	# 	else:
	# 		print("Right")
	# print(getHint(input_secret[-1], input_guess[-1]))

	#392
	# print(isSubsequence("acb", "ahbgdc"))

	#409
	# print(longestPalindrome("abccccdd"))

	#443
	# print(compress(["a"]))

	#459
	# print(repeatedSubstringPattern("ababababababaababababababaababababababa"))


	#482
	# print(licenseKeyFormatting("",1))

	#496
	# input_nums1 = [[4,1,2], [2,4], [1,3,5,2,4]]
	# input_nums2 = [[1,3,4,2], [1,2,3,4], [6,5,4,3,2,1,7]]
	# expected_output = [[-1,3,-1], [3,-1], [7,7,7,7,7]]
	# for i in range(len(input_nums1)):
	# 	if nextGreaterElement(input_nums1[i], input_nums2[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(nextGreaterElement(input_nums1[i], input_nums2[i]))
	# 	else:
	# 		print("Right")
	# print(nextGreaterElement(input_nums1[-1], input_nums2[-1]))

	#500
	# print(findWords(["Hello", "Alaska", "Dad", "Peace"]))