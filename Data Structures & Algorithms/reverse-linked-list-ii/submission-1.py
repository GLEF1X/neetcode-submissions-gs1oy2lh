# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prev = None
        curr = head
        counter = 1
        tailOfReversed = None
        prevOfTailOfReversed = None

        while curr and counter <= right:
            if counter < left:
                counter += 1
                prev = curr
                curr = curr.next
                continue
            
            if counter == left:
                tailOfReversed = curr 
                prevOfTailOfReversed = prev
            
            currNext = curr.next
            curr.next = prev
            prev = curr

            if counter == right:
                tailOfReversed.next = currNext
            curr = currNext
            counter += 1
        
        if prevOfTailOfReversed:
            prevOfTailOfReversed.next = prev

        if left > 1:
            return head
        
        return prev
