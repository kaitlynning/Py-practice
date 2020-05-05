class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

# skip duplicated node
# not duplicate of current node, move to next node

'''
Leetcode-Easy
83. Remove Duplicates from Sorted List
Runtime: 40 ms, faster than 75.67%
'''
