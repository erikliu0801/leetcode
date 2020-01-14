# ToDo:

"""
14. Longest Common Prefix
Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Note:

All given inputs are in lowercase letters a-z.

"""
# Concepts


# Code
## submit part
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
## test part

## code here
#1
"""
[]
"""
def longestCommonPrefix(strs):
	nums_shortest_str = 1000
	longest_common_prefix = ''
	for i, j in enumerate(strs):
		if nums_shortest_str > len(strs[i]):
			nums_shortest_str = len(strs[i])
	for i in range(nums_shortest_str-1):
		common = 0
		prefix = strs[0][i]
		for l in range(len(strs)):
			if strs[l][i] == prefix:
				common += 1
			else:
				break
		if common == len(strs):
			longest_common_prefix = longest_common_prefix + prefix
	return longest_common_prefix
#1.1
"""
["a"] => ok
Input:["c","c"]
Output:""
Expected:"c" => ok

Input:["aca","cba"]
Output:"a"
Expected:"" => ok

Success
Runtime: 32 ms, faster than 87.77% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Longest Common Prefix.
"""
def longestCommonPrefix(strs):
	if strs == []:
		return ''
	elif len(strs) == 1:
		return strs[0]
	else:
		nums_shortest_str = 1000
		longest_common_prefix = ''
		for i, j in enumerate(strs):
			if nums_shortest_str > len(strs[i]):
				nums_shortest_str = len(strs[i])
		else:
			for i in range(nums_shortest_str):
				common = 0
				prefix = strs[0][i]
				for l in range(len(strs)):
					if strs[l][i] == prefix:
						common += 1
					else:
						break
				if common == len(strs):
					longest_common_prefix = longest_common_prefix + prefix
				else:
					break		
		return longest_common_prefix


# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	input = [["flower","flow","flight"], ["dog","racecar","car"], [], ["a"], ["c","c"], ["aca","cba"]]
	expected_output = ["fl", "", "", "a", "c", ""]
	for i, j in enumerate(input):
		if longestCommonPrefix(input[i]) != expected_output[i]:
			print("Wrong!!!")
			print(longestCommonPrefix(input[i]))
		else:
			print("Right")

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