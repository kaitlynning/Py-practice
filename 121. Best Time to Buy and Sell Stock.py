class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float("inf")
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
            
        return max_profit
                    
'''
Leetcode-Easy
121. Best Time to Buy and Sell Stock
Runtime: 68 ms, faster than 45.45%


'''
