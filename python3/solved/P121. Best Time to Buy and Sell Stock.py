# ToDo:

"""
121. Best Time to Buy and Sell Stock
Easy

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Not 7-1 = 6, as selling price needs to be larger than buying price.

Example 2:

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
Input: [1,2]
Output: 2
Expected: 1 => solved
Misunderstanding (earn instead of sell_day)
"""
def maxProfit(prices):
	buy_val, earn, sell_day = float('inf'), 0, 0
	for day, val in enumerate(prices):
		if val < buy_val:
			buy_val = val
		if val - buy_val > earn and buy_val != 0:
			earn = val - buy_val
			sell_day = day + 1
	return sell_day

#1.1
"""
Input:[2,1,2,1,0,1,2]
Output:1
Expected:2

Success
Runtime: 60 ms, faster than 92.04% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Best Time to Buy and Sell Stock.
Next challenges: 
"""
def maxProfit(prices):
	buy_val, earn = float('inf'), 0
	for val in prices:
		if val < buy_val:
			buy_val = val
		if val - buy_val > earn:
			earn = val - buy_val
	return earn

# Test
## Functional Test
"""
# Conditions & Concepts

"""
if __name__ == '__main__':
	input_prices = [[7,1,5,3,6,4],[7,6,4,3,1],[7,1,5,3,6,4,1,8],[1,2],[2,1,2,1,0,1,2]]
	expected_output = [5,0,7,1,2]
	# for i in range(len(input_prices)):
	# 	if maxProfit(input_prices[i]) != expected_output[i]:
	# 		print("Wrong!!!")
	# 		print(maxProfit(input_prices[i]))
	# 	else:
	# 		print("Right")
	print(maxProfit(input_prices[-1]))
	

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