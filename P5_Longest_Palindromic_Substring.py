# ToDo:

"""
5. Longest Palindromic Substring
Medium

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"



"""
# Concepts


# Code
## submit part
class Solution:
	def longestPalindrome(self, s: str) -> str:
## test part
def longestPalindrome(s):

## code here
#1
def longestPalindrome(self,s):
	def IsPalindrome(substring): #ok
		answer = True
		half_len = len(substring)//2
		for i, j in enumerate(substring):
			if i >= half_len :
				if len(substring)%2 == 1:
					break
				else:
					break
			if substring[i] == substring[-1-i]:
				pass
			else:
				answer = False
		if answer != False:
			answer = True
		return answer
	# not right
	s_list = list(s)
	Palindromic_s = ""
	for i, j in enumerate(s_list):
		Palindromic_s = Palindromic_s + j
		if IsPalindrome(Palindromic_s) == True:
			pass
		else:
			for l in range(len(s_list)):

#1.1
# def longestPalindrome(self,s):
# 	def IsPalindrome(substring): #ok
# 		answer = True
# 		half_len = len(substring)//2
# 		for i, j in enumerate(substring):
# 			if i >= half_len :
# 				if len(substring)%2 == 1:
# 					break
# 				else:
# 					break
# 			if substring[i] == substring[-1-i]:
# 				pass
# 			else:
# 				answer = False
# 		if answer != False:
# 			answer = True
# 		return answer
# 	# not right
# 	for i in range(len(s)):
# 		if IsPalindrome(s[:]) == True:
# 			return s[:]
# 		else:
# 			for l in range(len(s)):
# 				if IsPalindrome(s[:]) == True:
# 					return s[:]
# 				else: 
# 					s = ([:-1])
# 			s = s[1:]
# 	return s

#1.2
"""
Time Limit Exceeded
"civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"
"""
def longestPalindrome(self,s):
	def IsPalindrome(substring): #ok
		answer = True
		half_len = len(substring)//2
		for i, j in enumerate(substring):
			if i >= half_len :
				if len(substring)%2 == 1:
					break
				else:
					break
			if substring[i] == substring[-1-i]:
				pass
			else:
				answer = False
		if answer != False:
			answer = True
		return answer
	# 
	palindrome_list = []
	for i in range(len(s)):
		if IsPalindrome(s) == True:
			palindrome_list.append(s)
			break
		else:
			s1 = s
			for l in range(len(s1)):
				if IsPalindrome(s1[:-1]) == True:
					palindrome_list.append(s1[:-1])
					break
				else: 
					s1 = s1[:-1]
			s = s[1:]
	answer = ""
	for i, j in enumerate(palindrome_list):
		if len(j) > len(answer):
			answer = j
	return answer

#1.3
"""
delelte only one string
wrong answer : "a",""
"""
def longestPalindrome(self,s):
	def IsPalindrome(substring): #ok
		answer = True
		half_len = len(substring)//2
		for i, j in enumerate(substring):
			if i >= half_len :
				if len(substring)%2 == 1:
					break
				else:
					break
			if substring[i] == substring[-1-i]:
				pass
			else:
				answer = False
		if answer != False:
			answer = True
		return answer
	# 
	palindrome_list = []
	for i in range(len(s)):
		if len(s) == 1:
			break
		elif IsPalindrome(s) == True:
			palindrome_list.append(s)
			break
		else:
			s1 = s
			for l in range(len(s1)):
				if len(s1) <= 2:
					break
				elif IsPalindrome(s1[:-1]) == True:
					palindrome_list.append(s1[:-1])
					break
				else: 
					s1 = s1[:-1]
			s = s[1:]
	answer = ""
	for i, j in enumerate(palindrome_list):
		if len(j) > len(answer):
			answer = j
	return answer

#1.4
def longestPalindrome(self,s):
	def IsPalindrome(substring): #ok
		answer = True
		half_len = len(substring)//2
		for i, j in enumerate(substring):
			if i >= half_len :
				if len(substring)%2 == 1:
					break
				else:
					break
			if substring[i] == substring[-1-i]:
				pass
			else:
				answer = False
		if answer != False:
			answer = True
		return answer
	# 
	if len(s) <= 1:
		return s
	else:
		if s.count(s[0])==len(s):
			return s
		else:		
			palindrome_list = []
			for i in range(len(s)):
				if len(s) == 1:
					break
				elif IsPalindrome(s) == True:
					palindrome_list.append(s)
					break
				else:
					s1 = s
					for l in range(len(s1)):
						if len(s1) <= 2:
							break
						elif IsPalindrome(s1[:-1]) == True:
							palindrome_list.append(s1[:-1])
							break
						else: 
							s1 = s1[:-1]
					s = s[1:]
			answer = ""
			for i, j in enumerate(palindrome_list):
				if len(j) > len(answer):
					answer = j
			return answer

# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
    substring_list = ["aba", "kfsgsfgfsgsfk","abcdefgfedcba","lkjkl"]
    for i, j in enumerate(substring_list):
        if IsPalindrome(substring_list[i]) == True:
            print("Right")
        else:
            print("Wrong!")

## Performance Test
import cProfile
cProfile.run('')


## Unit Test
import unittest
class Test(unittest.TestCase):
	def test(self):
		pass

if __name__ == '__main__':
	unittest.main()