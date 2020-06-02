class Solution:
    def trailingZeroes(self, n: int) -> int:
        result = 0
        
        while n != 0:
            result += n // 5
            n = n // 5
        return result
        
        
'''
Leetcode-Easy
172. Factorial Trailing Zeroes
Runtime: 20 ms, faster than 98.31%



'''
