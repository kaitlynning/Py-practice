class Solution:
    def titleToNumber(self, s: str) -> int:
        res = 0
        
        for i in s:
            res = res*26 + ord(i) - ord('A') + 1
        return res
        
'''
Leetcode-Easy
171. Excel Sheet Column Number
Runtime: 24 ms, faster than 95.77%



'''
