class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return len([x for x in nums if x<target])
        
    or
    
        if target > nums[len(nums) - 1]:
            return len(nums)
        
        for i in range(len(nums)):
            if nums[i] >=target:
                return i
 
        

'''
Leetcode-Easy
35. Search Insert Position
Runtime: 40 ms, faster than 98.21%
'''
