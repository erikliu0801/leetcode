# ToDo:

"""
9. Palindrome Number
Easy

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
# Concepts
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

# Code
## submit part
class Solution:
    def isPalindrome(self, x: int) -> bool:
## test part

## code here
#1
"""
Success
Runtime: 72 ms, faster than 53.32% of Python3 online submissions for Palindrome Number.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Palindrome Number.
Next challenges: 
"""
def isPalindrome(x):
	substring =str(x)
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

# Test
## Functional Test
"""
Condition:

"""
if __name__ == '__main__':
	input = [121, 1234, 1234321]
	expected_output = [True, False, True]
	for i, j in enumerate(input):
		if isPalindrome(input[i]) != expected_output[i]:
			print("Wrong!!!")
			print(isPalindrome(input[i]))
		else:
			print("Right")
	# print(myAtoi(input[2]))
	
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