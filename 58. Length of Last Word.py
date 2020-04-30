class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        local_count = 0
        
        for i in range(len(s)):
            if s[i] == ' ':
                local_count = 0 
            # 結尾了或重新開始（不知道哪種情況）
            else:
                local_count += 1
                count = local_count
            # 避免"Hello "空格返回0
        return count
'''
Leetcode-Easy
58. Length of Last Word
Runtime: 28 ms, faster than 65.92%
'''
