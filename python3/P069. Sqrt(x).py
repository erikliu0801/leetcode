# ToDo:

"""
69. Sqrt(x)
Easy

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
"""
# Conditions & Concepts
"""
* 0, 1
* negative number
* very big number
"""
# Code
## submit part
class Solution:
    def mySqrt(self, x: int) -> int:
## test part
def mySqrt(x):
	"""
	x: int
	rtype: int
	"""
## code here
#1 recursive reduce thne +=1
"""
Time Limit Exceeded => optimize
"""
def mySqrt(x):
	if x in [0,1]:
		return x
	else:
		try_num = x//2
		while try_num**2 >= x:
			if try_num**2 == x:
				return try_num
			else:
				try_num = try_num//2
		while try_num**2 <= x:
			if try_num**2 == x:
				return try_num
			else:
				try_num += 1
		try_num -= 1
		return try_num

#1.1
def mySqrt(x):
	if x < 0: #math.abs(x)
		x = 0 -x
	if x in [0,1]:
		return x
	else:
		try_num = x//2
		high_limit, low_limit = x, 0
		while try_num:
			if try_num**2 > x:
				if try_num == low_limit +1:
					answer = try_num
					break
				else:
					try_num = try_num//2
					high_limit = try_num
			elif try_num**2 < x:
				if try_num in [high_limit -1, high_limit] :
					answer = try_num
					break
				else:
					try_num = (try_num + high_limit)//2
					low_limit = try_num
			else:
				answer = try_num
				break
		return answer

#1.2
"""
Success
Runtime: 40 ms, faster than 65.39% of Python3 online submissions for Sqrt(x).
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Sqrt(x).
"""
def mySqrt(x):
	if x < 0: #math.abs(x)
		x = 0 -x
	if x in [0,1]:
		return x
	else:
		try_num = x//2
		high_limit, low_limit = x, 0
		answer = 0
		while answer < 1:
			if try_num**2 > x:
				high_limit = try_num
				if try_num == low_limit +1:
					answer = low_limit
					break
				else:
					try_num = (try_num + low_limit)//2						
			elif try_num**2 < x:
				low_limit = try_num
				if try_num in [high_limit -1, high_limit] :
					answer = try_num
					break
				else:
					try_num = (try_num + high_limit)//2
			else:
				answer = try_num
				break
		return answer

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_int = [4, 8, 0, 1, 2, 10000000, 1495504530]
	expected_output = [2, 2, 0, 1, 1, 3162, 38671]
	# for i in range(len(input_int)):
	# 	if mySqrt(input_int[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(mySqrt(input_int[i]))
	# 	else:
	# 		print("Right")
	print(mySqrt(input_int[-2]))
	

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