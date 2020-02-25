# ToDo:

"""
933. Number of Recent Calls
Easy

Write a class RecentCounter to count recent requests.

It has only one method: ping(int t), where t represents some time in milliseconds.

Return the number of pings that have been made from 3000 milliseconds ago until now.

Any ping with time in [t - 3000, t] will count, including the current ping.

It is guaranteed that every call to ping uses a strictly larger value of t than before.

Example 1:

Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
Output: [null,1,2,3,3] 

Note:
    Each test case will have at most 10000 calls to ping.
    Each test case will call ping with strictly increasing values of t.
    Each call to ping will have 1 <= t <= 10^9.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class RecentCounter:

    def __init__(self):
    	        

    def ping(self, t: int) -> int:
       


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
## test part

class RecentCounter:

    def __init__(self):
        

    def ping(self, t: int) -> int:
## code here
#1

class RecentCounter:

    def __init__(self):
        from collections import deque
    	self.queue = deque()

    def ping(self, t: int) -> int:
    	self.queue.append(t)
    	while self.queue[0] < t- 3000:
    		self.queue.popleft()
		return len(self.queue)

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