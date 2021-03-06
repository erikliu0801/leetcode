# ToDo:

"""
155. Min Stack
Easy

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

	push(x) -- Push element x onto stack.
	pop() -- Removes the element on top of the stack.
	top() -- Get the top element.
	getMin() -- Retrieve the minimum element in the stack.

 

Example:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();	  --> Returns 0.
minStack.getMin();   --> Returns -2.


"""
# Conditions & Concepts
"""

"""
# Code
## submit part
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class MinStack:

	def __init__(self):
		"""
		initialize your data structure here.
		"""
		

	def push(self, x: int) -> None:
		

	def pop(self) -> None:
		

	def top(self) -> int:
		

	def getMin(self) -> int:
## test part
class MinStack:
	def __init__(self):


	def push(self, x):
		

	def pop(self):
		

	def top(self):
		

	def getMin(self):

## code here
#1
"""
Success
Details
Runtime: 808 ms, faster than 19.94% of Python3 online submissions for Min Stack.
Memory Usage: 16.1 MB, less than 100.00% of Python3 online submissions for Min Stack.
"""
class MinStack:
	def __init__(self):
		self.stack = []
	def push(self, x):
		self.stack.append(x)
	def pop(self):
		self.stack.pop()
	def top(self):
		return self.stack[-1]
	def getMin(self):
		return min(self.stack)

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