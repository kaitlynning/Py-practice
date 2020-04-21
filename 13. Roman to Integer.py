class Solution:
    def romanToInt(self, s):
        romanMap = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        ans = 0
        for i in range(len(s)):
            if i<len(s)-1 and romanMap[s[i+1]] > romanMap[s[i]]:
                ans -= romanMap[s[i]]
            else:
                ans += romanMap[s[i]]
        return ans
        
        print(ans)

'''
Leetcode-Easy
13. Roman to Integer
'''
