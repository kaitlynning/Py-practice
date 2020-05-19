class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        #利潤加買進差值
        return profit
        
'''
Leetcode-Easy
122. Best Time to Buy and Sell Stock II
Runtime: 72 ms, faster than 30.75%


'''
