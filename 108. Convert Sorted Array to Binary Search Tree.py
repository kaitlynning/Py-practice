# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def to_bst(nums, start, end):
            if start > end:
                return None

            mid = (start + end) // 2

            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root
        return to_bst(nums, 0, len(nums)-1)
        
        
'''
Leetcode-Easy
108. Convert Sorted Array to Binary Search Tree
Runtime: 76 ms, faster than 53.46%
'''
