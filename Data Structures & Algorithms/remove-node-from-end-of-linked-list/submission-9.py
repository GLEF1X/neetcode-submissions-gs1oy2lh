# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slowPtr = head
        fastPtr = head
        currElementPosition = 1
        # [1,2,3,4], n = 2

        while fastPtr.next:
            if currElementPosition > n:
                slowPtr = slowPtr.next
                
            fastPtr = fastPtr.next
            currElementPosition += 1

        
        if currElementPosition == n:
            return head.next

        slowPtr.next = slowPtr.next.next

        return head