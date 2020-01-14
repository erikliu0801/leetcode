# ToDo:

"""
412. Fizz Buzz
Easy

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
## test part
def fizzBuzz(n):
	"""
	n: int
	rtype: List[str]
	"""
## code here
#1
# def fizzBuzz(n):
# 	str_nums = list()
# 	import math
# 	for i in range(1,n+1):
# 		if 15**int(math.log(i,15)) == i and i != 1:
# 			str_nums.append('FizzBuzz')
# 		elif 3**int(math.log(i,3)) == i and i != 1:
# 			str_nums.append('Fizz')
# 		elif 5**int(math.log(i,5)) == i and i != 1:
# 			str_nums.append('Buzz')
# 		else:
# 			str_nums.append(str(i))
# 	return str_nums

#1.1
"""
Success
Runtime: 36 ms, faster than 96.01% of Python3 online submissions for Fizz Buzz.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Fizz Buzz.
"""
def fizzBuzz(n):
	str_nums = list()
	for i in range(1,n+1):
		if i%15 == 0:
			str_nums.append('FizzBuzz')
		elif i%3 == 0:
			str_nums.append('Fizz')
		elif i%5 == 0:
			str_nums.append('Buzz')
		else:
			str_nums.append(str(i))
	return str_nums

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