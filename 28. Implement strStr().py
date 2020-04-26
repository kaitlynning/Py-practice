class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i 
        return -1
        
# range(n) function doesn't actually include number n. You have to actually use +1 in order to reach n

'''
Leetcode-Easy
28. Implement strStr()
Runtime: 32 ms, faster than 51.55.%
'''
