class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
        # input 999
        # output 000 ->100 -> 1000
            else:
                digits[i] += 1
                return digits
        digits[0] = 1
        digits.append(0)
        return digits
        
'''
Leetcode-Easy
66. Plus One
Runtime: 28 ms, faster than 84.66%
'''
