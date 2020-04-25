class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0 
        last = len(nums)-1
        while i <= last:
            if nums[i] == val:
                nums.pop(i)
                last -= 1
            else:
                i += 1
        return len(nums) 


'''
Leetcode-Easy
27. Remove Element
Runtime: 32 ms, faster than 63.47%
'''
