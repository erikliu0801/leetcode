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
    mid1, mid2 = len(nums1) // 2, len(nums2) // 2
    answer = 0
    while answer == 0:
        if nums1[mid1] > nums2[mid2]:
            # nums1 to left
            mid1 = mid1 // 2
            # nums2 to right
            mid2 = mid2 * 3 // 2
        elif nums1[mid1] < nums2[mid2]:
            # nums2 to left
            mid2 = mid2 // 2
            # nums1 to right
            mid1 = mid1 * 3 // 2

        else:
            answer = nums1[mid1]
    return answer

if __name__ == "__main__":
    # string01: str = "abcabcbb"
    # string02 = " "
    # string03 = "dvdf"
    # print(lengthOfLongestSubstring(string03))
    nums1 = [3]
    nums2 = [1,2,5]
    print(findMedianSortedArrays(nums1,nums2))
