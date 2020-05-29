class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        
        nums[:k], nums[k:] = nums[len(nums) - k: ], nums[: len(nums) - k]
        
        
'''
Leetcode-Easy
189. Rotate Array
Runtime: 60 ms, faster than 82.69%



'''
