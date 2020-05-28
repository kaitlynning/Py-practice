# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        array = [] #build an array 
        
        def inorder(node): 
            if not node:
                return
            
            inorder(node.left)
            array.append(node.val) #add an array
            inorder(node.right)
        
        inorder(root)  
        
        return array[k-1]  #bec 0 index, we are looking for kth element
        

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.counter = 1  #create/initalize self variables
        self.k_smallest = None  #always valid
        
        def inorder(node): #helper function we call inorder
            if not node or self.k_smallest:
                return
            #sorted/structured order
            inorder(node.left)
            if self.counter == k: 
                self.k_smallest = node.val #set our caller function into this value
            self.counter += 1 #otherwise increase our counter(where we are at)
            inorder(node.right)
        
        inorder(root)  #Traverse the left sub-tree, (recursively call inorder(root -> left). Visit and print the root node. Traverse the right sub-tree, (recursively call inorder(root -> right).
        
        return self.k_smallest #return value of kth 
        #we structure in inorder # sort through the entire tree
'''
Leetcode-Easy
230. Kth Smallest Element in a BST
Runtime: 48 ms, faster than 90.65%



'''
