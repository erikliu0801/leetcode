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
"""
"ac","bb",""abcda""
Time Limit Exceeded => same situation with 1.2
"""
	def longestPalindrome(self,s):
		def IsPalindrome(substring):
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
		elif len(s) == 2:
			if s[0] != s[1]:
				return s[0]
			else:
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
				if answer == "":
					return s[0]
				else:	
					return answer
#2 slice a string into several substring
def CutSubstring2List(s:str): => list	
	def SubstringCountList(substring):
		substring_count_list = []
		for i, j  in enumerate(substring):
			substring_count_list.append(substring.count(substring[i]))
		return substring_count_list
	substring_list =[]
	y = SubstringCountList(s)
	s1 = s
	l=0
	count = 0
	for i, j in enumerate(substring_count_list):
		if j == 1:
			if len(s) > i +1:
				substring_list.append(s[l:i+1])
			substring_list.append(s[i])
			if len(s) <= i +1:
				s1 = s[i+1:]
		else:
			count +=1
	substring_list.append(s1)
	return substring_list

#2.1
def longestPalindrome(s):
	def SubstringCountList(self,s):
		substring_count_list = []
		for i, j  in enumerate(substring):
			substring_count_list.append(substring.count(substring[i]))
		return substring_count_list

	substring_count_list = SubstringCountList(s)
	def CutSubstring2List(self,s,substring_count_list):		
		substring_list =[]
		s1 = s
		l=0
		count = 0
		for i, j in enumerate(substring_count_list):
			if j == 1:
				if len(s) > i +1:
					substring_list.append(s[l:i+1])
				substring_list.append(s[i])
				if len(s) <= i +1:
					s1 = s[i+1:]
			else:
				count +=1
		substring_list.append(s1)
		return substring_list

#2.2

def longestPalindrome(s):
	def SubstringCountList(s):
		substring_count_list = []
		for i, j  in enumerate(s):
			substring_count_list.append(s.count(s[i]))
		return substring_count_list

	substring_count_list = SubstringCountList(s)
	
	def CutSubstring2CombinedList(s,substring_count_list):		
		substring_list =[]
		s1 = s
		l=0
		count = 0
		#
		for i, j in enumerate(SubstringCountList(s)):
			if j == 1 and s[l:i] != "":
				if len(s) > i +1:
					substring_list.append(s[l:i])
				substring_list.append(s[i])
				s1 = s[i+1:]
				l = i+1
			else:
				count +=1
		if s1 != '':
			substring_list.append(s1)
		#Combine	
		for i, j in enumerate(substring_list):
			if len(substring_list[i])==1 and i-1 >= 0 and i+2 <= len(substring_list):
				#
				if len(substring_list[i-1]) != 1 and len(substring_list[i+1]) != 1:
					if substring_list[i-1][-1] == substring_list[i+1][0]:
						substring_list[i] = substring_list[i-1] +substring_list[i] +substring_list[i+1]
		if substring_list == []:
			substring_list = [""]
		return substring_list
	return CutSubstring2CombinedList(s, substring_count_list)	
"""
['a', 'b', 'a', 'y', 'g', 'h', 'd', 'f', 'g']
['sfhsfkfsgsfgfsgsfkjgddjdhjh']
['a']
['']
['c', 'a']
['bb']
['a', 'b', 'c', 'd', 'a']
['civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeare', 'q', 'metonagreatbattlefiemldoft', 'z', 'hatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothis', 'B', 'utinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsder', 'G', 'odshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth']
"""

#2.3
"""
input: "babad"
Output: "d"
Expected: "bab"
=> optimize Fuc CutSubstring2CombinedList OK

input: "abayghdfg"
Output: "a"
Expected: "aba"
=> optimize Fuc CutSubstring2CombinedList OK

input: "aba"
Output: "a"
Expected: "aba"
=> optimize Fuc RecursiveCheckStringList OK

Time Limit Exceeded
"ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"
no count"1" obejcts!! => change algorithm
"""
def longestPalindrome(s):
	def SubstringCountList(s):
		substring_count_list = []
		for i, j  in enumerate(s):
			substring_count_list.append(s.count(s[i]))
		return substring_count_list
	def CutSubstring2CombinedList(s,substring_count_list): #ok	
		substring_list =[]
		s1 = s
		l=0
		count = 0
		#
		for i, j in enumerate(SubstringCountList(s)):
			if j == 1 and s[l:i] != "":
				if len(s) >= i +1:
					substring_list.append(s[l:i])
				substring_list.append(s[i])
				s1 = s[i+1:]
				l = i+1
			else:
				count +=1
		if s1 != '':
			substring_list.append(s1)
		#Combine	
		for i, j in enumerate(substring_list):
			if len(substring_list[i])==1 and i-1 >= 0 and i+2 <= len(substring_list):
				#
				if substring_list[i-1] != 1 and substring_list[i+1] != 1:
					if substring_list[i-1][-1] == substring_list[i+1][0]:
						substring_list[i] = substring_list[i-1] +substring_list[i] +substring_list[i+1]
		if substring_list == []:
			substring_list = [""]
		return substring_list
	#IsPalindrome
	def IsPalindrome(substring):
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
	#Recursive Test
	def RecursiveCheckStringList(substring_list): #
		palindrome_list = []
		for l, s in enumerate(substring_list):
			for i, j in enumerate(s):
				if s.count(s[0])==len(s):
					palindrome_list.append(s)
				else:
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
		if answer == "" and s != "":
			return s[0]
		elif s =="":
			return s
		else:
			return answer

	substring_count_list = SubstringCountList(s)
	substring_list = CutSubstring2CombinedList(s, substring_count_list)
	answer = RecursiveCheckStringList(substring_list)
	if answer == None:
		answer = ''
	return answer

#3 
"""
Algorithm:
* Reverse
* Expand Around Center
* Manacher's Algorithm
"""
"""
input: "eabcb"
Output: "e"
Expected: "bcb"
"""
def longestPalindrome(s):
	palindrome_list = []
	s1 = s
	for i, j in enumerate(s):
		s2 = s1
		for l, k in enumerate(s1):
			if s1[0] != s2[-1]:
				s2 = s2[:-1]
			else:
				palindrome_list.append(s2) #
		s1 = s1[i+1:]
	answer = ""
	for i, j in enumerate(palindrome_list):
		if len(j) > len(answer):
			answer = j
	if answer == "" and s != "":
		return s[0]
	elif s =="":
		return s
	else:
		return answer

#3.1
def longestPalindrome(s):
	palindrome_list = []
	s1 = s
	for i in range(len(s)):
		s2 = s1
		for l in range(len(s1)):
			if s1[0] == s2[-1]:
				count = 0
				for m in range(len(s2)):
					if s2[-1-m] == s1[m]:
						count += 1
					else:
						break
				s1 = s1[i+1:]
				if count == len(s2):
					palindrome_list.append(s2)
					break
			else:				
				s2 = s2[:-1] #
	answer = ""
	for i, j in enumerate(palindrome_list):
		if len(j) > len(answer):
			answer = j
	if answer == "" and s != "":
		return s[0]
	elif s =="":
		return s
	else:
		return answer

#3.2
"""
Time Limit Exceeded
Last executed input:
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
"""
def longestPalindrome(s):
	palindrome_list = []
	s1 = s
	for i in range(len(s)):
		s2 = s1
		for l in range(len(s1)):
			if s1[0] == s2[-1]:
				count = 0
				for m in range(len(s2)):
					if s2[-1-m] == s1[m]:
						count += 1
					else:
						break				
				if count == len(s2):
					palindrome_list.append(s2)
					break
				else:
					s2 = s2[:-1]
			else:				
				s2 = s2[:-1]
		s1 = s1[1:]
	answer = ""
	for i, j in enumerate(palindrome_list):
		if len(j) > len(answer):
			answer = j
	if answer == "" and s != "":
		return s[0]
	elif s =="":
		return s
	else:
		return answer

#3.3
"""
Runtime Error
''
"""
def longestPalindrome(s):
	palindrome_list = []
	s1 = s
	j1 = s[0]
	l = 0
	for i, j in enumerate(s):
		if j != j1:
			j1 = j
			if len(s[l:i]) > 1:
				palindrome_list.append(s[l:i])
			l = i
		elif i+1 == len(s) and j1 == j:
			palindrome_list.append(s[l:i+1])
	step2 = True
	for j in palindrome_list:
		if len(j)>len(s)%3:			
			step2 = False
			break
	if step2 == True:
		s1 = s
		for i in range(len(s)):
			s2 = s1
			for l in range(len(s1)):
				if s1[0] == s2[-1]:
					count = 0
					for m in range(len(s2)):
						if s2[-1-m] == s1[m]:
							count += 1
						else:
							break				
					if count == len(s2):
						palindrome_list.append(s2)
						break
					else:
						s2 = s2[:-1]
				else:				
					s2 = s2[:-1]
			s1 = s1[1:]
	answer = ""
	for i, j in enumerate(palindrome_list):
		if len(j) > len(answer):
			answer = j
	if answer == "" and s != "":
		return s[0]
	elif s =="":
		return s
	else:
		return answer

#3.4
"""
'cbbd' => ok
'abadd' => step1 need to be optimized => ok
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabcaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
"""
def longestPalindrome(s):
	palindrome_list = []
	step1, step2 = False, True
	if len(s)<5:
		if len(s)<=1:
			palindrome_list.append(s)
		elif 1<len(s) and len(s)<4 and s[0]==s[-1]:
			palindrome_list.append(s)
		elif len(s)==4 and s[1]==s[-2] and s[0]==s[-1]:
			palindrome_list.append(s)
		else:
			palindrome_list.append(s[0])
	else:
		step1 = True
	if step1 == True:
		j1 = s[0]
		l = 0
		for i, j in enumerate(s):
			if j != j1:
				j1 = j
				if len(s[l:i]) > 1:
					palindrome_list.append(s[l:i])
				l = i
			elif i+1 == len(s) and j1 == j:
				palindrome_list.append(s[l:i+1])
		for j in palindrome_list:
			if len(j)>len(s)/2: #		
				step2 = False
				break
			# elif :
	if step2 == True:
		s1 = s
		for i in range(len(s)):
			s2 = s1
			for l in range(len(s1)):
				if s1[0] == s2[-1]:
					count = 0
					for m in range(len(s2)):
						if s2[-1-m] == s1[m]:
							count += 1
						else:
							break				
					if count == len(s2):
						palindrome_list.append(s2)
						break
					else:
						s2 = s2[:-1]
				else:				
					s2 = s2[:-1]
			s1 = s1[1:]
	answer = ""
	for i, j in enumerate(palindrome_list):
		if len(j) > len(answer):
			answer = j
	if answer == "" and s != "":
		return s[0]
	elif s =="":
		return s
	else:
		return answer

#4


# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
   # P_substring_list = ["aba", "kfsgsfgfsgsfk"]
	substring_list = ["aba","abayghdfg","sfhsfkfsgsfgfsgsfkjgddjdhjh","a","","ca","bb","abcda","babad","civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth",
	"ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"]
	
	substring_count_list = [
			[2, 1, 2, 1, 2, 1, 1, 1, 2],
			[6, 6, 3, 6, 6, 2, 6, 6, 4, 6, 6, 4, 6, 6, 4, 6, 6, 2, 3, 4, 3, 3, 3, 3, 3, 3, 3],
			[1],
			[],	
			[1, 1],	
			[2, 2],	
			[2, 1, 1, 1, 2], 
			[25, 53, 22, 53, 41, 23, 87, 67, 106, 142, 40, 106, 53, 61, 23, 23, 74, 142, 106, 74, 142, 67, 106, 74, 87, 106, 61, 87, 16, 106, 53, 78, 61, 78, 67, 87, 61, 8, 61, 87, 67, 106, 53, 78, 	61, 40, 78, 25, 78, 61, 25, 142, 53, 22, 142, 52, 87, 61, 52, 40, 78, 52, 142, 52, 53, 25, 87, 106, 142, 52, 25, 87, 61, 41, 78, 61, 23, 142, 61, 52, 17, 67, 142, 2, 142, 87, 67, 142, 1, 13, 142, 106, 78, 61, 87, 23, 67, 142, 87, 106, 11, 87, 106, 106, 41, 142, 26, 53, 142, 13, 41, 52, 78, 26, 106, 1, 74, 87, 106, 23, 87, 67, 2, 142, 74, 87, 22, 142, 25, 78, 13, 142, 106, 78, 52, 142, 52, 53, 25, 16, 87, 106, 142, 87, 16, 78, 67, 106, 53, 78, 61, 78, 26, 106, 74, 87, 106, 26, 53, 142, 41, 52, 87, 40, 87, 26, 53, 61, 87, 41, 67, 142, 40, 106, 53, 61, 23, 16, 41, 87, 25, 142, 26, 78, 67, 106, 74, 78, 40, 142, 23, 74, 78, 74, 142, 67, 42, 23, 87, 22, 142, 106, 74, 142, 53, 67, 41, 53, 22, 142, 40, 106, 74, 87, 106, 106, 74, 87, 106, 61, 87, 106, 53, 78, 61, 13, 53, 23, 74, 106, 41, 53, 22, 142, 3, 106, 53, 40, 87, 41, 106, 78, 23, 142, 106, 74, 142, 67, 26, 87, 61, 23, 87, 61, 52, 16, 67, 78, 16, 142, 67, 106, 74, 87, 	106, 23, 142, 40, 74, 78, 17, 41, 52, 52, 78, 106, 74, 53, 40, 1, 17, 106, 53, 61, 87, 41, 87, 67, 23, 142, 67, 40, 142, 61, 40, 142, 23, 142, 25, 87, 61, 61, 78, 106, 52, 142, 52, 53, 25, 87, 106, 142, 23, 142, 25, 87, 61, 61, 78, 106, 25, 78, 61, 40, 142, 25, 67, 87, 106, 142, 23, 142, 25, 87, 61, 61, 78, 106, 74, 87, 41, 41, 78, 23, 106, 74, 53, 40, 23, 67, 78, 17, 61, 52, 2, 74, 142, 11, 67, 87, 22, 142, 41, 13, 142, 61, 41, 53, 22, 53, 61, 23, 87, 61, 52,	52, 142, 87, 52, 23, 74, 78, 40, 106, 67, 17, 23, 23, 41, 142, 52, 74, 142, 67, 142, 74, 87, 22, 142, 25, 78, 61, 40, 142, 25, 67, 87, 106, 142, 52, 53, 106, 26, 87, 67, 87, 11, 78, 22, 142, 78, 17, 67, 16, 78, 78, 67, 16, 78, 61, 23, 142, 67, 106, 78, 87, 52, 52, 78, 67, 52, 142, 106, 67, 87, 25, 106, 2, 23, 74, 142, 23, 78, 67, 41, 52, 87, 52, 40, 23, 26, 53, 41, 41, 41, 53, 106, 106, 41, 142, 61, 78, 106, 41, 142, 61, 78, 67, 41, 78, 61, 23, 67, 142, 13, 142, 13, 11, 142, 67, 23, 74, 87, 106, 23, 142, 40, 87, 8, 74, 142, 67, 142, 11, 17, 106, 53, 106, 25, 87, 61, 61, 142, 22, 142, 67, 26, 78, 67, 23, 142, 106, 23, 74, 87, 106, 106, 74, 142, 8, 52, 53, 52, 74, 142, 67, 142, 3, 106, 53, 40, 26, 78, 67, 17, 40, 106, 74, 142, 41, 53, 22, 53, 61, 23, 67, 87, 106, 74, 142, 67, 106, 78, 11, 142, 52, 142, 52, 53, 25, 87, 106, 142, 52, 74, 142, 67, 142, 106, 78, 106, 74, 142, 17, 41, 61, 26, 53, 61, 53, 40, 74, 142, 52, 23, 78, 67, 3, 23, 74, 53, 25, 74, 106, 74, 142, 8, 23, 74, 78, 26, 78, 17, 23, 74, 106, 74, 142, 67, 142, 74, 87, 22, 142, 106, 74, 17, 40, 26, 87, 67, 40, 78, 61, 78, 11, 41, 8, 87, 52, 	22, 87, 61, 25, 142, 52, 3, 106, 53, 40, 67, 87, 106, 74, 142, 67, 26, 78, 67, 17, 40, 106, 78, 11, 142, 74, 142, 67, 142, 52, 142, 52, 53, 25, 87, 106, 142, 52, 106, 78, 106, 74, 142, 23, 67, 142, 87, 106, 106, 52, 87, 26, 40, 3, 67, 142, 13, 87, 53, 61, 53, 61, 23, 11, 142, 26, 78, 67, 142, 17, 40, 106, 74, 87, 106, 26, 67, 78, 13, 106, 74, 142, 40, 142, 74, 78, 61, 78, 67, 142, 52, 52, 142, 87, 52, 23, 142, 106, 87, 3, 142, 53, 61, 25, 67, 142, 87, 40, 142, 52, 52, 142, 22, 78, 106, 53, 78, 61, 106, 78, 106, 74, 87, 106, 25, 87, 17, 40, 142, 26, 78, 67, 23, 74, 53, 25, 74, 106, 74, 142, 8, 23, 87, 22, 142, 106, 74, 142, 41, 87, 40, 106, 16, 26, 17, 41, 41, 13, 142, 87, 40, 17, 67, 142, 78, 26, 52, 142, 22, 78, 106, 53, 78, 61, 106, 74, 87, 106, 23, 142, 74, 142, 67, 142, 74, 53, 23, 74, 41, 8, 67, 142, 40, 78, 41, 22, 142, 106, 74, 87, 106, 106, 74, 142, 40, 142, 52, 142, 87, 52, 40, 74, 87, 41, 41, 61, 78, 106, 74, 87, 22, 142, 52, 53, 142, 52, 53, 61, 22, 87, 53, 61, 106, 74, 87, 106, 106, 74, 53, 40, 61, 87, 106, 53, 78, 61, 17, 61, 40, 52, 142, 67, 1, 78, 52, 40, 74, 87, 41, 41, 74, 87, 22, 142, 87, 61, 142, 23, 11, 53, 67, 106, 74, 78, 26, 26, 67, 142, 142, 52, 78, 13, 87, 61, 52, 106, 74, 87, 106, 23, 78, 22, 142, 67, 61, 13, 142, 61, 106, 78, 26, 106, 74, 142, 16, 142, 78, 16, 41, 142, 11, 8, 106, 74, 142, 16, 142, 78, 16, 41, 142, 26, 78, 67, 106, 74, 142, 16, 142, 78, 16, 41, 142, 40, 74, 87, 41, 41, 61, 78, 106, 16, 142, 67, 53, 40, 74, 26, 67, 78, 13, 106, 74, 142, 142, 87, 67, 106, 74]
		]

    # for i, j in enumerate(substring_list):
    #     if IsPalindrome(substring_list[i]) == True:
    #         print("Right")            
    #     else:
    #         print("Wrong!")
    
    # for i, j in enumerate(P_substring_list):
    #     print(longestPalindrome(P_substring_list[i]))

	for i, j in enumerate(substring_list):
		print(longestPalindrome(substring_list[i]))

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