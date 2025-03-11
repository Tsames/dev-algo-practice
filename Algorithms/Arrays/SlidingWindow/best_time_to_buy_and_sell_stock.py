'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


Constraints:
1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        '''
        Strategy:
        Declare a variable, res, to hold the greatest difference we can find in prices.
        Declare a left pointer, l, and use it to keep track of the price we want to buy at (starting at 0).
        Declare a right pointer, r, and use it to keep track of the price we want to sell at (starting at 1).

        Iterate through our list, incrementing the right pointer each time.
            Calculate and save the difference, r - l, to a variable diff.

            If the difference between our left and right pointer is negative, that indicates the element
            at the right pointer is smaller than the element at the right pointer.
                So, move our left pointer to the smaller value, since we want to buy when the price is low.

            Otherwise, set prices to be whichever value is greater, itself or the new difference we just calculated.
            Then increment the right pointer.

        Finally, once the loop is done, return res.
        '''
        res = 0

        l, r = 0, 1
        while r < len(prices):
            diff = prices[r] - prices[l]
            if diff < 0:
                l = r
            else:
                res = max(res, diff)
            r += 1

        return res


solution = Solution()
assert solution.maxProfit([7,1,5,3,6,4]) == 5, "Test one failed."
assert solution.maxProfit([7,6,4,3,1]) == 0, "Test two failed."
assert solution.maxProfit([1, 0]) == 0, "Test three failed."




