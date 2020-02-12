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

# def main():
# 	for i in range(1,31):
# 		print(fib(i))


#605
def canPlaceFlowers(flowerbed, n):
	rest_place = []
	max_added_flowers = 0
	existed_flowers = flowerbed.count(1)
	while flowerbed:
		if flowerbed[0] == 1:
			flowerbed = flowerbed[2:]
			existed_flowers -= 1
			continue
		if existed_flowers > 0:
			rest_place.append(flowerbed[:flowerbed.index(1)-1])
			flowerbed = flowerbed[flowerbed.index(1)+2:]
			existed_flowers -= 1
		else:
			rest_place.append(flowerbed)
			break
	for place in rest_place:
		max_added_flowers += (len(place)+1) // 2
	return n <= max_added_flowers

# def main():
# 	input_flowerbed = [[1,0,0,0,1], [1,0,0,0,1], [1,0,1,0,1,0,1], [1,0,1,0,1,0,0,1], [1,0,1,0,1,0,0,0,1], [1,0,0,0,1,0,0]]
# 	input_n = [1, 2, 1, 1, 1, 2]
# 	expected_output = [True, False, False, False, True, True]
# 	for i in range(len(input_flowerbed)):
# 		if canPlaceFlowers(input_flowerbed[i], input_n[i]) != expected_output[i]:
# 			print("Wrong!!!", ' Output:', canPlaceFlowers(input_flowerbed[i], input_n[i]), '; Expected Output:', expected_output[i])
# 		else:
# 			print("Right")
# 	print(canPlaceFlowers(input_flowerbed[-1], input_n[-1]))

#643
def findMaxAverage(nums, k):
	if k == 1: return max(nums)
	max_sum = sum(nums[:k])/k
	rest_prob = len(nums) - k
	mean = max_sum
	for i in range(rest_prob):
		mean += (nums[k+i] - nums[i]) / k
		max_sum = max(max_sum, mean)
	return max_sum

# def main():
# 	input_nums = [[1,12,-5,-6,50,3]]
# 	input_k = [4]
# 	expected_output = [12.75]
# 	for i in range(len(input_nums)):
# 		if findMaxAverage(input_nums[i], input_k[i]) != expected_output[i]:
# 			print("Wrong!!!", ' Output:', findMaxAverage(input_nums[i], input_k[i]), '; Expected Output:', expected_output[i])
# 		else:
# 			print("Right")
	# print(findMaxAverage(input_nums[-1], input_k[-1]))

#665
def checkPossibility(nums):
	nums0 = nums.copy()
	for i in range(1,len(nums)):
		if nums[i] < nums[i-1]:
			nums[i-1] = nums[i]
			new_nums_sorted = nums.copy()
			new_nums_sorted.sort()
			nums0[i] = nums0[i-1]
			new_nums0_sorted = nums0.copy()
			new_nums0_sorted.sort()
			return nums == new_nums_sorted or nums0 == new_nums0_sorted
	return True

# def main():
# 	input_nums = [[1,2,3],[4,2,3],[4,2,1],[3,4,2,3],[2,3,3,2,4]]
# 	expected_output = [True, True, False, False, True]
# 	for i in range(len(input_nums)):
# 		if checkPossibility(input_nums[i]) != expected_output[i]:
# 			print("Wrong!!!", ' Output:', checkPossibility(input_nums[i]), '; Expected Output:', expected_output[i])
# 		else:
# 			print("Right")
# 	print(checkPossibility(input_nums[-1]))

#674
def findLengthOfLCIS(nums):
	if len(nums) < 2:
		return len(nums)
	count = 1
	nums_count = []
	for i in range(1,len(nums)):
		if nums[i] > nums[i-1]:
			count += 1
			if i == len(nums) -1:
				nums_count.append(count)
		else:
			nums_count.append(count)
			count = 1
	return max(nums_count)

# def main():
# 	input_nums = [[1,3,5,4,7], [2,2,2,2,2], [1,3,5,7]]
# 	expected_output = [3, 1, 4]
# 	for i in range(len(input_nums)):
# 		if findLengthOfLCIS(input_nums[i]) != expected_output[i]:
# 			print("Wrong!!!", ' Output:', findLengthOfLCIS(input_nums[i]), '; Expected Output:', expected_output[i])
# 		else:
# 			print("Right")
	# print(findLengthOfLCIS(input_nums[-1]))


#680
def validPalindrome(s):
	if s == s[::-1]: return True
	i = 0
	while i <= len(s)//2:
		if s[i] != s[-1-i]:
			s1 = s[:i] + s[i+1:]
			s2 = s[:-1-i] + s[len(s)-i:]
			return s1 == s1[::-1] or s2 == s2[::-1]
		i += 1

# def main():
# 	input_s = ["abccba","dabccba","abccbad","dabcdfcba"]
# 	expected_output = [True, True, True, False]
# 	for i in range(len(input_s)):
# 		if validPalindrome(input_s[i]) != expected_output[i]:
# 			print("Wrong!!! Output:", validPalindrome(input_s[i]))
# 		else:
# 			print("Right")
# 	print(validPalindrome(input_s[2]))

#717
def isOneBitCharacter(bits):
	cd = False
	for bit in bits[:-1]:
		if cd :
			cd = False
			continue
		if bit == 1:
			cd = True
	return not cd

# def main():
# 	input_bits = [[1, 0, 0], [1, 1, 1, 0], [0], [1, 0], [0, 0]]
# 	expected_output = [True, False, True, False, True]
# 	for i in range(len(input_bits)):
# 		if isOneBitCharacter(input_bits[i]) != expected_output[i]:
# 			print("Wrong!!!", ' Output:', isOneBitCharacter(input_bits[i]), '; Expected Output:', expected_output[i])
# 		else:
# 			print("Right")
# 	print(isOneBitCharacter(input_bits[1]))

#724
def pivotIndex(nums):
	for i in range(len(nums)):
		if sum(nums[:i]) == sum(nums[i+1:]): return i
	return -1

# def main():
# 	input_nums = [[1, 7, 3, 6, 5, 6], [1, 2, 3], [1,2,-2]]
# 	expected_output = [3, -1, 0]
# 	for i in range(len(input_nums)):
# 		if pivotIndex(input_nums[i]) != expected_output[i]:
# 			print("Wrong!!!", ' Output:', pivotIndex(input_nums[i]), '; Expected Output:', expected_output[i])
# 		else:
# 			print("Right")
	# print(pivotIndex(input_nums[-1]))

#747
def dominantIndex(nums):
	a = max(nums)
	i = nums.index(a)
	nums.remove(a)
	return i if a >= (max(nums)*2) else -1

def main():
	input_nums = [[3, 6, 1, 0], [1, 2, 3, 4], [0,0,0,1]]
	expected_output = [1, -1, 3]
	for i in range(len(input_nums)):
		if dominantIndex(input_nums[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', dominantIndex(input_nums[i]), '; Expected Output:', expected_output[i])
		else:
			print("Right")
	# print(dominantIndex(input_nums[0]))


#804
def uniqueMorseRepresentations(words):
	morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
	alph = [chr(x) for x in range(97,123)]
	m_a = {alph[i]:morse[i] for i in range(26)}
	morse_strs = []
	for word in words:
		morse_str = ''
		for w in word.lower():
			morse_str += m_a[w]
		morse_strs.append(morse_str)
	return len(set(morse_strs))

# def main():
# 	input_words = [["gin", "zen", "gig", "msg"]]
# 	expected_output = [2]
# 	for i in range(len(input_words)):
# 		if uniqueMorseRepresentations(input_words[i]) != expected_output[i]:
# 			print("Wrong!!!")
# 			print(uniqueMorseRepresentations(input_words[i]))
# 		else:
# 			print("Right")
	# print(uniqueMorseRepresentations(input_words[-1]))

#819
def mostCommonWord(paragraph, banned):
	from collections import Counter
	alph = [chr(x) for x in range(97, 123)]
	words = []
	word = ''
	for w in paragraph:
		if w.lower() in alph:
			word += w.lower()
		elif word != '':
			words.append(word)
			word = ''
	if word != '':
		words.append(word)
	frequence = Counter(words)
	while frequence:
		frequentest, _ = frequence.most_common(1)[0]
		if frequentest not in banned:
			return frequentest
		frequence.pop(frequentest)
	return ''

# def main():
# 	input_paragraph = ["Bob hit a ball, the hit BALL flew far after it was hit.", "Bob"]
# 	input_banned = [["hit"], []]
# 	expected_output = ["ball", "bob"]
# 	for i in range(len(input_paragraph)):
# 		if mostCommonWord(input_paragraph[i], input_banned[i]) != expected_output[i]:
# 			print("Wrong!!!")
# 			print(mostCommonWord(input_paragraph[i], input_banned[i]))
# 		else:
# 			print("Right")
# 	print(mostCommonWord(input_paragraph[-1], input_banned[-1]))

#824
def toGoatLatin(S):
	word = ''
	w_end = ''
	transed_S = ''
	index = 1
	vowel = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
	up = set([chr(x) for x in range(65,91)])
	low = set([chr(x) for x in range(97,123)])
	for c in (S+' '):
		if word == '' and w_end == '':
			if c in vowel:
				word = c
			if c in ((up | low) - vowel):
				w_end = c
		elif c in (up | low):
			word += c
		else:
			if word != '' or w_end != '':
				transed_S += word + w_end + 'ma' + ('a' * index)
				index += 1
				word, w_end = '', ''
			transed_S += c
	return transed_S[:-1]

# def main():
# 	input_S = ["I speak Goat Latin", "The quick brown fox jumped over the lazy dog", "HZ sg L"]
# 	expected_output = ["Imaa peaksmaaa oatGmaaaa atinLmaaaaa", "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa", "ZHmaa gsmaaa Lmaaaa"]
# 	for i in range(len(input_S)):
# 		if toGoatLatin(input_S[i]) != expected_output[i]:
# 			print("Wrong!!!", ' Output:', toGoatLatin(input_S[i]), '; Expected Output:', expected_output[i])
# 		else:
# 			print("Right")
	# print(toGoatLatin(input_S[-1]))

#859
def buddyStrings(A, B):
	if set(A) != set(B) or len(A) < 2 or len(B) < 2:
		return False
	if A == B :
		from collections import Counter
		a = Counter(A)
		if a.most_common(1)[0][1] >=2:
			return True
		return False
	a_b = None
	for a, b in zip(A, B):
		if a != b:
			if a_b:
				if a != a_b[1] or b != a_b[0]:
					return False
			a_b = (a,b)
	if a_b:
		return True
	else:
		return False

# def main():
# 	input_A = ["ab", "ab", "aa", "aaaaaaabc", ""]
# 	input_B = ["ba", "ab", 'aa', "aaaaaaacb", "aa"]
# 	expected_output = [True, False, True, True, False]
# 	for i in range(len(input_A)):
# 		if buddyStrings(input_A[i], input_B[i]) != expected_output[i]:
# 			print("Wrong!!!", ' Output:', buddyStrings(input_A[i], input_B[i]), '; Expected Output:', expected_output[i])
# 		else:
# 			print("Right")
	# print(buddyStrings(input_A[-1], input_B[-1]))

#917
def reverseOnlyLetters(S):
	i_c = {}
	up = set([chr(x) for x in range(65,91)])
	low = set([chr(x) for x in range(97,123)])
	reversed_nums = list()
	for i, c in enumerate(S):
		if c in (up | low):
			reversed_nums.append(c)
		else:
			i_c[i] = c
	reversed_nums.reverse()
	for i in i_c:
		reversed_nums.insert(i, i_c[i])
	reversed_S = ''
	for c in reversed_nums : reversed_S += c
	return reversed_S

# def main():
# 	input_S = ["ab-cd", "a-bC-dEf-ghIj", "Test1ng-Leet=code-Q!"]
# 	expected_output = ["dc-ba", "j-Ih-gfE-dCba", "Qedo1ct-eeLg=ntse-T!"]
# 	for i in range(len(input_S)):
# 		if reverseOnlyLetters(input_S[i]) != expected_output[i]:
# 			print("Wrong!!!", ' Output:', reverseOnlyLetters(input_S[i]), '; Expected Output:', expected_output[i])
# 		else:
# 			print("Right")
	# print(reverseOnlyLetters(input_S[-1]))

#925
def isLongPressedName(name, typed):
	if name == typed: return True
	if set(name) != set(typed): return False
	last = ''
	j = 0
	for i, nc in enumerate(name):
		while j < len(typed):
			if typed[j] == nc:
				j += 1
				break
			elif typed[j] == last:
				j += 1
			else : return False
		if i < len(name) and j == len(typed) and typed[j-1] != nc: return False #
		last = nc
	rest = set(typed[j:])
	if rest:
		if len(rest) > 1 : return False
		return True if last in rest else False
	return True

# def main():
# 	input_name = ["alex", "saeed", "leelee", "laiden", "kikcxmvzi", "izi"]
# 	input_typed = ["aaleex", "ssaaedd", "lleeelee", "laiden", "kiikcxxmmvvzz", "izz"]
# 	expected_output = [True, False, True, True, False, False]
# 	for i in range(len(input_name)):
# 		if isLongPressedName(input_name[i], input_typed[i]) != expected_output[i]:
# 			print("Wrong!!!", ' Output:', isLongPressedName(input_name[i], input_typed[i]), '; Expected Output:', expected_output[i])
# 		else:
# 			print("Right")
# 	print(isLongPressedName(input_name[-1], input_typed[-1]))

#929
def numUniqueEmails(emails):
	local_name = ''
	uniqe_emails = set()
	for email in emails:
		for i, c in enumerate(email):
			if c == '.':
				continue
			elif c == '+':
				uniqe_emails.add(local_name + email[email.index('@'):])
				local_name = ''
				break
			elif c == '@':
				uniqe_emails.add(local_name + email[i:])
				local_name = ''
				break
			else:
				local_name += c
	return len(uniqe_emails)

# def main():
# 	input_emails = [["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]]
# 	expected_output = [2]
# 	for i in range(len(input_emails)):
# 		if numUniqueEmails(input_emails[i]) != expected_output[i]:
# 			print("Wrong!!!", ' Output:', numUniqueEmails(input_emails[i]), '; Expected Output:', expected_output[i])
# 		else:
# 			print("Right")
	# print(numUniqueEmails(input_emails[-1]))

if __name__ == "__main__":
	import time
	t_start = time.time()
	main()
	print(time.time()-t_start)

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
