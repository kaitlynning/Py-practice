class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, (len(s)-1)
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1 #往右
            j -= 1 #往左
        return True
    '''
    isalnum 檢查 alphanumeric文字或數字
    isalpha 只檢查文字
    
    '''
        
'''
Leetcode-Easy
125. Valid Palindrome
Runtime: 56 ms, faster than 36.23%


'''
