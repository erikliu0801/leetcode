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
	def SubstringCountList(s):
		substring_count_list = []
		for i, j  in enumerate(s):
			substring_count_list.append(s.count(s[i]))
		return substring_count_list

	substring_count_list = SubstringCountList(s)
	
	def CutSubstring2List(s,substring_count_list):		
		substring_list =[]
		s1 = s
		l=0
		count = 0
		for i, j in enumerate(SubstringCountList(s)):
			if j == 1:
				if len(s) > i +1 and s[l:i] != "":
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
				if len(substring_list[i-1]) != 1 and len(substring_list[i+1]) != 1:
					if substring_list[i-1][-1] == substring_list[i+1][0]:
						substring_list[i] = substring_list[i-1] +substring_list[i] +substring_list[i+1]
		return substring_list
	
	return CutSubstring2List(s, substring_count_list)
	
	


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
	substring_list = ["abayghdfg","sfhsfkfsgsfgfsgsfkjgddjdhjh","a","","ca","bb","abcda","civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"]
	
    # for i, j in enumerate(substring_list):
    #     if IsPalindrome(substring_list[i]) == True:
    #         print("Right")            
    #     else:
    #         print("Wrong!")
    
    # for i, j in enumerate(P_substring_list):
    #     print(longestPalindrome(P_substring_list[i]))

	for i, j in enumerate(substring_list):
		print(longestPalindrome(substring_list[i]))
	
	# print(longestPalindrome(substring_list[2]))
	
	# for i, j in enumerate(substring_list):
	# 	print(SubstringCountList(substring_list[i]))