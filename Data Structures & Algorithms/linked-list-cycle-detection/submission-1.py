# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowCurr = head
        fastCurr = head
        isCycle = False

        while fastCurr:
            slowCurr = slowCurr.next
            intermediateFastCurr = fastCurr.next
            if not intermediateFastCurr:
                return False
            fastCurr = intermediateFastCurr.next
            
            if slowCurr == fastCurr:
                isCycle = True
                break

        return isCycle