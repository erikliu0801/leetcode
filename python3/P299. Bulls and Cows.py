# ToDo:

"""
299. Bulls and Cows
Easy
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        
## test part
def getHint(secret, guess):
	"""
	secret: str
	guess: str
	rtype: str
	"""
## code here
#1
"""
Runtime Error
Last executed input
"11"
"11"

len(secret) = len(guess)
"""
# def getHint(secret, guess):
# 	if guess == '':
# 		return '0A0B'
# 	elif secret == guess:
# 		return str(len(secret)) + 'A0B'
# 	bulls, cows = 0, 0
# 	bulls_position = list()
# 	secret, guess = list(secret)[::-1], list(guess)[::-1]
# 	for i, num in enumerate(secret):
# 		if num == guess[i]:
# 			bulls += 1
# 			bulls_position.append(i)
# 		if i+1 == len(guess):
# 			break
# 	for i in bulls_position: #
# 		secret.pop(i)
# 		guess.pop(i)
# 	for num in guess:
# 		if num in secret:
# 			cows += 1
# 			secret.remove(num)
# 	return str(bulls) + 'A' + str(cows) + 'B'

#1.1
"""
Wrong Answer
Input: "9305"
"9205"
Output: "2A1B"
Expected: "3A0B"
"""
# def getHint(secret, guess):
# 	if guess == '':
# 		return '0A0B'
# 	elif secret == guess:
# 		return str(len(secret)) + 'A0B'
# 	bulls, cows = 0, 0
# 	secret, guess = list(secret), list(guess)
# 	for s_num, g_num in zip(secret,guess):
# 		if s_num == g_num:
# 			bulls += 1
# 			secret.remove(s_num)
# 			guess.remove(g_num)
# 	for num in guess:
# 		if num in secret:
# 			cows += 1
# 			secret.remove(num)
# 	return str(bulls) + 'A' + str(cows) + 'B'

#1.2
"""
Runtime Error
ValueError: Expected object or value

Success
Runtime: 96 ms, faster than 5.00% of Python3 online submissions for Bulls and Cows.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Bulls and Cows.
"""
def getHint(secret, guess):
	if guess == '':
		return '0A0B'
	elif secret == guess:
		return str(len(secret)) + 'A0B'
	bulls, cows = 0, 0
	secret, guess = list(secret), list(guess)
	s_g_nums = list()
	for s_g in zip(secret,guess):
		s_g_nums.append(s_g)
	secret, guess = list(), list()
	for s_num, g_num in s_g_nums.copy():
		if s_num == g_num:
			bulls +=1
			s_g_nums.remove((s_num,g_num))
		else:
			secret.append(s_num)
			guess.append(g_num)
	for num in guess:
		if num in secret:
			cows += 1
			secret.remove(num)
	return str(bulls) + 'A' + str(cows) + 'B'

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_secret = ["1807", "1123", "11"]
	input_guess = ["7810", "0111", "11"]
	expected_output = ["1A3B", "1A1B", "2A0B"]
	for i in range(len(input_secret)):
		if getHint(input_secret[i], input_guess[i]) != expected_output[i]:
			print("Wrong!!!")
			print(getHint(input_secret[i], input_guess[i]))
		else:
			print("Right")		
	# print(getHint(input_secret[-1], input_guess[-1]))
	

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