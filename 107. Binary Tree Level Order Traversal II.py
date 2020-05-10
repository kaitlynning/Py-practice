class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        result, current = [], [root]
        
        while current:
            next_level, vals = [], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current = next_level
            result.append(vals)
            
        return result[::-1]
        
        #因為要有一個[]放最終結果，分析每個收件人還是不是有左右分支，而且還要把它記錄到vals裡去，有了cur，result裡添加的數字有[]所以有了vals ，因為cur也要更新所以用而循環清空他，還要next_level去更新它
'''
Leetcode-Easy
107. Binary Tree Level Order Traversal II
Runtime: 28 ms, faster than 93.37%
'''
