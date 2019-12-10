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
	substring_list = ["abayghdfg","sfhsfkfsgsfgfsgsfkjgddjdhjh","a","","civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"]
    # for i, j in enumerate(substring_list):
    #     if IsPalindrome(substring_list[i]) == True:
    #         print("Right")            
    #     else:
    #         print("Wrong!")
    
    # for i, j in enumerate(P_substring_list):
    #     print(longestPalindrome(P_substring_list[i]))

	for i, j in enumerate(substring_list):
		print(longestPalindrome(substring_list[i]))