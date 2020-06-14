class Solution:
    def rob(self, nums: List[int]) -> int:
        last, now = 0, 0
        for num in nums:
            #cannot be two adjacent
            last, now = now, max(last+num, now)
        return now
        
'''
Leetcode-Easy
198. House Robber
Runtime: 32 ms, faster than 56.33%



'''
