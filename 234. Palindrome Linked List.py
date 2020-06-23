# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = ListNode(0)
        fast = slow = head
        stack = []
        #split in half from the middle
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            #two times faster 
            fast = fast.next.next
            
        if fast:
            slow = slow.next
        
        while slow:
            top = stack.pop()
            
            if top != slow.val:
                return False
            slow = slow.next
        return True
            
            
        
'''
Leetcode-Easy
234. Palindrome Linked List
Runtime: 68 ms, faster than 85.46%



'''
