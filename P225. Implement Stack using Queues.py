# ToDo:

"""
225. Implement Stack using Queues
Easy
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class MyStack:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		

	def push(self, x: int) -> None:
		"""
		Push element x onto stack.
		"""
		

	def pop(self) -> int:
		"""
		Removes the element on top of the stack and returns that element.
		"""
		

	def top(self) -> int:
		"""
		Get the top element.
		"""
		

	def empty(self) -> bool:
		"""
		Returns whether the stack is empty.
		"""
		


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

## test part

## code here
#1
"""
Runtime: 28 ms, faster than 75.98% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Implement Stack using Queues.
"""
class MyStack:
	def __init__(self):
		self.stack = []

	def push(self, x: int) -> None:
		self.stack.append(x)

	def pop(self) -> int:
		return self.stack.pop()

	def top(self) -> int:
		return self.stack[-1]

	def empty(self) -> bool:
		return self.stack == []

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