class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)
        local_max, global_max = 0, 0
        for num in nums:
            local_max = max(0, local_max + num)
            global_max = max(global_max, local_max)
        return global_max

'''
Leetcode-Easy
53. Maximum Subarray
Runtime: 64 ms, faster than 81.22%
'''
