# ToDo:

"""
122. Best Time to Buy and Sell Stock II
Easy

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
# Conditions & Concepts
"""

"""
# Code
## submit part
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
## test part
def maxProfit(prices):
	"""
	prices: List[int]
	rtype: int
	"""
## code here
#1
"""
serveral times maxProfit()
def maxProfit(prices):
	buy_val, earn = float('inf'), 0
	for val in prices:
		if val < buy_val:
			buy_val = val
		if val - buy_val > earn:
			earn = val - buy_val
	return earn


Success
Runtime: 56 ms, faster than 96.77% of Python3 online submissions for Best Time to Buy and Sell Stock II.
Memory Usage: 13.9 MB, less than 68.29% of Python3 online submissions for Best Time to Buy and Sell Stock II.
"""
def maxProfit(prices):
	buy_val, earn, earn_sum = float('inf'), 0, 0
	for val in prices:
		if val < buy_val:
			buy_val = val
		if val - buy_val > earn:
			earn = val - buy_val
		elif val - buy_val < earn:
			earn_sum += earn
			buy_val, earn = val, 0
	earn_sum += earn
	return earn_sum

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_prices = [[7,1,5,3,6,4],[1,2,3,4,5],[7,6,4,3,1]]
	expected_output = [7,4,0]
	for i in range(len(input_prices)):
		if maxProfit(input_prices[i]) != expected_output[i]:
			print("Wrong!!!")
			print(maxProfit(input_prices[i]))
		else:
			print("Right")		
	# print(maxProfit(input_prices[-1]))
	

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