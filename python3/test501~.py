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
