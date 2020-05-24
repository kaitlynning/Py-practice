# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        point1 = headA
        point2 = headB
        
        while point1 != point2:
            if not point1:
                point1 = headB
            else:
                point1 = point1.next
                
            if not point2:
                point2 = headA
            else:
                point2 = point2.next
        return point2

'''
Leetcode-Easy
160. Intersection of Two Linked Lists
Runtime: 172 ms, faster than 60.25%

'''
