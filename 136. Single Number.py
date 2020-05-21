class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        
        for num in nums:
            ans ^= num
            #XOR（互斥exclusive）運算符號^
        return ans
        
'''
Leetcode-Easy
136. Single Number
Runtime: 84 ms, faster than 83.44%


'''
