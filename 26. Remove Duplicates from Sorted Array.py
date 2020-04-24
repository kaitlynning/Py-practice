class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        count = 0
        for i in range(len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
        
        return count +1


'''
Leetcode-Easy
26. Remove Duplicates from Sorted Array
Runtime: 80 ms, faster than 90.10%
'''
