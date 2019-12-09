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

def findMedianSortedArrays(nums1, nums2):
    def Combine2SortedArrays(l1,l2):			
        # if len(l2)>len(l1): #l1 should be longer
        # if l2[0]<l1[0]: #l2[0] should be smaller
        #     l1, l2 = l2, l1
        l0 = []
        for i, j in enumerate(l2):
            for l, k in enumerate(l1):
                if k < j:
                    l0.append(k)
                else:
                    l0.append(j)
                    break 
            if len(l1) <= l +1:
                l1 = []
            else:
                l1 = l1[l+1:]
            if len(l2) <= i +1:
                l2 = []
            else:
                l2 = l2[i:]
            l0.append(j)
        return l0
    nums_combined = Combine2SortedArrays(nums1,nums2)
    if len(nums_combined)%2 == 1:
        return float(nums_combined[len(nums_combined)//2])
    else:
        return (nums_combined[len(nums_combined)//2]+nums_combined[(len(nums_combined)//2)-1])/2.0


if __name__ == "__main__":
   # string01: str = "abcabcbb"    # string02 = " "
    # string03 = "dvdf"
    # print(lengthOfLongestSubstring(string03))
    
    
    
    nums10 = [3]
    nums20 = [1,2,5]
    nums30 = 2.5
    
    nums11 =[1,2]
    nums21 =[3,4]
    nums31 = 2.5

    nums12 =[1,2,7,8]
    nums22 =[3,4,5]
    nums32 = 4.0

    nums1 = nums12
    nums2 = nums22
    nums3 =  nums32

    print("nums1= %s ,nums2= %s " %(nums1, nums2))
    if nums3 != findMedianSortedArrays(nums11,nums21):
        print("Wrong Answer! Expect:%s, Output%s"%(nums3, findMedianSortedArrays(nums11,nums21)))
    else:
        print("Right Answer! %s"%(findMedianSortedArrays(nums11,nums21)))
