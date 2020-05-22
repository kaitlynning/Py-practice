# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast, slow = head, head
        
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast == slow:
                return True
        else:
            return False
'''
Leetcode-Easy
141. Linked List Cycle
Runtime: 48 ms, faster than 70.57%

'''
