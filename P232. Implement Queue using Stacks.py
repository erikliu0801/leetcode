# ToDo:

"""
232. Implement Queue using Stacks
Easy
Implement the following operations of a queue using stacks.

push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
Example:

MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class MyQueue:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		

	def push(self, x: int) -> None:
		"""
		Push element x to the back of queue.
		"""
		

	def pop(self) -> int:
		"""
		Removes the element from in front of queue and returns that element.
		"""
		

	def peek(self) -> int:
		"""
		Get the front element.
		"""
		

	def empty(self) -> bool:
		"""
		Returns whether the queue is empty.
		"""
		


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

## test part

## code here
"""
Success
Runtime: 28 ms, faster than 78.02% of Python3 online submissions for Implement Queue using Stacks.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Implement Queue using Stacks.
"""
#1
class MyQueue:
	def __init__(self):
		self.queue = []

	def push(self, x: int) -> None:
		self.queue.insert(0,x)

	def pop(self) -> int:
		return self.queue.pop()

	def peek(self) -> int:
		if len(self.queue) > 0:
			return self.queue[-1]

	def empty(self) -> bool:
		return self.queue == []

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