# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        nums = []
        
        self.preTraversal(root, nums)
        #preordertraversal(root, left, right)
        ans = nums[1] - nums[0]
        for i in range(1, len(nums)):
            ans = min(ans, nums[i] - nums[i - 1])
        #if nums[i] - nums[i - 1] 小於min_abs 就去取代之前的值
        return ans

    def preTraversal(self, root, nums):
        if not root:
            return
        self.preTraversal(root.left, nums)
        nums.append(root.val)
        self.preTraversal(root.right, nums)
        
        
'''
Leetcode-Easy
530. Minimum Absolute Difference in BST
Runtime: 60 ms, faster than 53.35%
經典

'''
