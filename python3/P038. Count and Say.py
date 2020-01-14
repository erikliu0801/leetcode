# ToDo:

"""
38. Count and Say
Easy

The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
1211 => "one 1, one 2, two 1s" or 11 12 21

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Explanation: This is the base case.

Example 2:

Input: 4
Output: "1211"
Explanation: For n = 3 the term was "21" in which we have two groups "2" and "1", "2" can be read as "12" which means frequency = 1 and value = 2, the same way "1" is read as "11", so the answer is the concatenation of "12" and "11" which is "1211".



"""
# Concepts


# Code
## submit part
class Solution:
    def countAndSay(self, n: int) -> str:

## test part
def countAndSay(n):
	"""
	n: int; 1 ≤ n ≤ 30
	rtype: str
	"""

## code here
#1
def countAndSay(n):
	start = '1'
	if n > 1:
		answer = ''
		for i in range(n):
			count = 1
			for i in range(len(start)):
				if start[i] == start[i-1] and i < len(start):
					count += 1
				else :
					answer = answer + str(count) + str(start[i])
					count = 1
			if count > 1:
				answer = answer + str(count) + str(start[i])
		return answer
	else:
		return start

#1.1
"""
Success
Runtime: 32 ms, faster than 90.56% of Python3 online submissions for Count and Say.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Count and Say.
"""
def countAndSay(n):
	start = '1'
	if n > 1:
		# answer = ''
		for m in range(n-1):
			count = 1
			answer, repeat = '', ''
			for i in range(len(start)):
				if i == 0:
					repeat = start[i]
				elif start[i] == repeat:
					count += 1
				elif start[i] != repeat:
					answer = answer + str(count) + str(start[i-1])
					repeat = start[i]
					count = 1
			answer = answer + str(count) + str(start[-1])
			start = answer
		return answer
	else:
		return start



# Test
## Functional Test
"""
Condition:

1.     1
2.     11
3.     21
4.     1211
5.     111221
"""
if __name__ == '__main__':
    input1 = [1, 2, 3, 4, 5, 6, 7, 8]
    expected_output = ["1", "11", "21", "1211", "111221", "312211", "13112221", "1113213211"]

    # for i, j in enumerate(input1):
    #     if countAndSay(input1[i]) != expected_output[i]:
    #         print("Wrong!!!")
    #         print(countAndSay(input1[i]))
    #     else:            
    #         print("Right")
    print(countAndSay(input1[3]))
	

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