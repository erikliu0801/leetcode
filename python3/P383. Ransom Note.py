# ToDo:

"""
383. Ransom Note
Easy
Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
## test part
def canConstruct(ransomNote, magazine):
	"""
	ransomNote: str
	magazine: str
	rtype: bool
	"""
## code here
#1
"""
Input:"fffbfg"
"effjfggbffjdgbjjhhdegh"
Output: false
Expected: true
"""
def canConstruct(ransomNote, magazine):
	return ransomNote in magazine

#1.1
"""
Success
Runtime: 36 ms, faster than 93.67% of Python3 online submissions for Ransom Note.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Ransom Note.
"""
def canConstruct(ransomNote, magazine):
	if set(ransomNote) - set(magazine) != set():
		return False
	for alphabet in set(ransomNote):
		if ransomNote.count(alphabet) > magazine.count(alphabet):
			return False
	return True

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input1 = []
	expected_output = []
	for i in range(len(input1)):
		if func(input1[i]) != expected_output[i]:
			print("Wrong!!!")
			print(func(input1[i]))
		else:
			print("Right")		
	# print(func(input1[-1]))
	

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