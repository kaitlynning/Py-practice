# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        point1 = headA
        point2 = headB
      #if a & b have different len, then we will stop the loop after second iteration  
        while point1 != point2:
            #循環條件 直到p1不等於p2 就一直去做循環了
            if not point1:
                point1 = headB
            else:
                point1 = point1.next
      #for the end of first iteration, we just reset the pointer to the head of another linkedlist         
            if not point2:
                point2 = headA
            else:
                point2 = point2.next
        return point2

'''
Leetcode-Easy
160. Intersection of Two Linked Lists
Runtime: 172 ms, faster than 60.25%

 don't care about the "value" of difference, we just want to make sure two pointers reach the intersection node at the same time.
 
'''
