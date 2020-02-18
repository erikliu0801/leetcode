# ToDo:

"""
1237. Find Positive Integer Solution for a Given Equation
Easy

Given a function  f(x, y) and a value z, return all positive integer pairs x and y where f(x,y) == z.

The function is constantly increasing, i.e.:

f(x, y) < f(x + 1, y)
f(x, y) < f(x, y + 1)

The function interface is defined like this: 

interface CustomFunction {
public:
  // Returns positive integer f(x, y) for any given positive integer x and y.
  int f(int x, int y);
};

For custom testing purposes you're given an integer function_id and a target z as input, where function_id represent one function from an secret internal list, on the examples you'll know only two functions from the list.  

You may return the solutions in any order.

Constraints:
1 <= function_id <= 9
1 <= z <= 100
It's guaranteed that the solutions of f(x, y) == z will be on the range 1 <= x, y <= 1000
It's also guaranteed that f(x, y) will fit in 32 bit signed integer if 1 <= x, y <= 1000
"""
# Conditions & Concepts
"""
f(x, y) < f(x + 1, y)
f(x, y) < f(x, y + 1)

1 <= z <= 100
"""
# Code
## submit part
"""
This is the custom function interface.
You should not implement it, or speculate about its implementation
class CustomFunction:
   # Returns f(x, y) for any given positive integers x and y.
   # Note that f(x, y) is increasing with respect to both x and y.
   # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
   def f(self, x, y):  
"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
## test part
def findSolution(customfunction, z):
	"""
	customfunction: 'CustomFunction'
	z: int
	rtype: List[List[int]]:
	"""
## code here
#1
"""
Time Limit Exceeded
"""
def findSolution(customfunction, z):
	res = []
	for x in range(1,101):
		for y in range(1,1001):
			if customfunction.f(x,y) == z:
				res.append([x,y])
	return res

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_customfunction = []
	input_z = []
	expected_output = []
	for i in range(len(input1)):
		if func(input1[i]) != expected_output[i]:
			print("Wrong!!!", ' Output:', func(input1[i]), '; Expected Output:', expected_output[i])
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