class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        num = n
        
        while n > 0:
            y = (n - 1) % 26
            n = (n - 1) // 26
            s = chr(y + ord('A'))
            res = ''.join((s, res))
            
        return res
        
        
'''
Leetcode-Easy
168. Excel Sheet Column Title
Runtime: 28 ms, faster than 74.43% 

chr CHARACTER


'''
