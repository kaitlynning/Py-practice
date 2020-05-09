class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
'''
Leetcode-Easy
104. Maximum Depth of Binary Tree
Runtime: 40 ms, faster than 71.38%
'''
