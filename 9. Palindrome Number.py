class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_1 = str(abs(x))
        str_2 = str_1[::-1]
        if str_1 == str_2:
            return True
        else:
            return False

'''
Leetcode-Easy
9. Palindrome Number
'''
