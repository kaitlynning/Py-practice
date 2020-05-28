# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        array = []
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            array.append(node.val)
            inorder(node.right)
        
        inorder(root)  
        
        return array[k-1]
        
        
'''
Leetcode-Easy
230. Kth Smallest Element in a BST
Runtime: 48 ms, faster than 90.65%



'''
