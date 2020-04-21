class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        str = ""
        for i in list(zip(*strs)):
            if len(set(i)) == 1:
                str += i[0]
            else:
                break
        return str

'''
Leetcode-Easy
14. Longest Common Prefix
'''
