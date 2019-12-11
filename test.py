def lengthOfLongestSubstring(s):
    unrepeated_substring = []
    substring = ""
    for i, j in enumerate(list(s)):  #
        if substring.count(j) == 0:
            substring = substring + j
        else:
            unrepeated_substring.append(substring)
            for i, k in enumerate(list(substring)):
                if k == j:
                    sub_substring = ""
                    for y in list(substring)[i + 1:]:
                        sub_substring = sub_substring + y
                    substring = sub_substring + j
                    break
    unrepeated_substring.append(substring)
    max_count = 0
    for i, _ in enumerate(unrepeated_substring):
        count = len(unrepeated_substring[i])
        if count > max_count:
            max_count = count
    return max_count

#P4
def findMedianSortedArrays(nums1, nums2):
	def Combine2SortedArrays(l1,l2):
		l0 = []
		if l1 == []:
			l1, l2 = l2, l1
		for i, j in enumerate(l1):
			if l2 != []:
				if j < l2[0]:
					l0.append(j)
					l1 = l1[1:]
				else:
					for l, k in enumerate(l2):
						if k < j:
							l0.append(k)
							l2 = l2[1:]
						else:
							l0.append(j)
							l1 = l1[1:]
							break
					if l2 == []:
						l0.append(j)
						l1 = l1[1:]
			else:
				l0.append(j)
				l1 = l1[1:]
		for k in l2:
			l0.append(k)
		return l0

	nums_combined = Combine2SortedArrays(nums1,nums2)
	if len(nums_combined)%2 == 1:
		return float(nums_combined[len(nums_combined)//2])
	else:
		return (nums_combined[len(nums_combined)//2]+nums_combined[(len(nums_combined)//2)-1])/2.0

#5
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
			if len(j)>len(s)/2:			
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
	
#6
def convert(s, numRows):
	#
	if numRows == 1:
		answer = s
	else:
		needed_List = []
		for i in range(numRows):
			needed_List.append([])
		#
		onetime_steps = numRows *2 -2
		for i, j in enumerate(list(s)):
			numofStep = i%onetime_steps
			if numofStep < numRows :
				needed_List[numofStep].append(j)
			else:
				l = numofStep - numRows
				needed_List[-2-l].append(j) #numRows>2
		#
		answer =''
		for i, j in enumerate(needed_List):
			for i in needed_List[i]:
				answer += i
	return answer

#7
def reverse(x):
	#
	negative = False
	if x < 0:
		x = -x
		negative = True
	#
	reverse_str = []
	for i in range(len(str(x))):
		reverse_str.append(str(x)[-1-i])
	revers_x = ''
	for j in reverse_str:
		revers_x = revers_x + j
	revers_x = int(revers_x)
	if negative==True:
		revers_x = 0 - revers_x
	if revers_x<-2**31 or revers_x>2**31-1:
		revers_x = 0
	return revers_x

#8

if __name__ == "__main__":
   # string01: str = "abcabcbb"    # string02 = " "
    # string03 = "dvdf"
    # print(lengthOfLongestSubstring(string03))
    
    
    # # P4
    # nums0 = [[[3],[1,2,5],2.5]
    # nums1 = [[1,2],[3,4],2.5]
    # nums2 = [[1,2,7,8],[3,4,5],4.0]
    # nums3 = [[3,4,5],[1,2,7,8],4.0]

    # nums1, nums2, nums3 = nums3[0:]

    # print("nums1= %s ,nums2= %s " %(nums1, nums2))
    # if nums3 != findMedianSortedArrays(nums1,nums2):
    #     print("Wrong Answer! Expect:%s, Output%s"%(nums3, findMedianSortedArrays(nums1,nums2)))
    # else:
    #     print("Right Answer! %s"%(findMedianSortedArrays(nums1,nums2)))

    #5
    # P_substring_list = ["aba", "kfsgsfgfsgsfk"]
	# substring_list = ["aba","abayghdfg","sfhsfkfsgsfgfsgsfkjgddjdhjh","a","","ca","bb","abcda","babad","civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth","ibvjkmpyzsifuxcabqqpahjdeuzaybqsrsmbfplxycsafogotliyvhxjtkrbzqxlyfwujzhkdafhebvsdhkkdbhlhmaoxmbkqiwiusngkbdhlvxdyvnjrzvxmukvdfobzlmvnbnilnsyrgoygfdzjlymhprcpxsnxpcafctikxxybcusgjwmfklkffehbvlhvxfiddznwumxosomfbgxoruoqrhezgsgidgcfzbtdftjxeahriirqgxbhicoxavquhbkaomrroghdnfkknyigsluqebaqrtcwgmlnvmxoagisdmsokeznjsnwpxygjjptvyjjkbmkxvlivinmpnpxgmmorkasebngirckqcawgevljplkkgextudqaodwqmfljljhrujoerycoojwwgtklypicgkyaboqjfivbeqdlonxeidgxsyzugkntoevwfuxovazcyayvwbcqswzhytlmtmrtwpikgacnpkbwgfmpavzyjoxughwhvlsxsgttbcyrlkaarngeoaldsdtjncivhcfsaohmdhgbwkuemcembmlwbwquxfaiukoqvzmgoeppieztdacvwngbkcxknbytvztodbfnjhbtwpjlzuajnlzfmmujhcggpdcwdquutdiubgcvnxvgspmfumeqrofewynizvynavjzkbpkuxxvkjujectdyfwygnfsukvzflcuxxzvxzravzznpxttduajhbsyiywpqunnarabcroljwcbdydagachbobkcvudkoddldaucwruobfylfhyvjuynjrosxczgjwudpxaqwnboxgxybnngxxhibesiaxkicinikzzmonftqkcudlzfzutplbycejmkpxcygsafzkgudy"]
	
    # for i, j in enumerate(substring_list):
    #     if IsPalindrome(substring_list[i]) == True:
    #         print("Right")            
    #     else:
    #         print("Wrong!")
    
    # for i, j in enumerate(P_substring_list):
    #     print(longestPalindrome(P_substring_list[i]))

	# for i, j in enumerate(substring_list):
	# 	print(longestPalindrome(substring_list[i]))
	
	# print(longestPalindrome(substring_list[-1]))
	# print(longestPalindrome('abadd'))

	#6
	# string = ["PAYPALISHIRING","PAYPALISHIRING"]
	# numRows = [3, 4]
	# expected_output = ["PAHNAPLSIIGYIR","PINALSIGYAHRPI"]
	# print(convert(string[1],numRows[1]))

	#7
	# x = [123, -123, 120, 1534236469, 900000, 1463847412]
	# expected_output = [321, -321, 21, 0, 9, 2147483641]
	# for i, j in enumerate(x):
	# 	print(reverse(x[i]))

	#8
