# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1Curr = l1
        l2Curr = l2
        dummy = ListNode()
        curr = dummy
        counter = 1
        carryover = 0
        
        while l1Curr or l2Curr:
            val = carryover
            if l1Curr:
                val += l1Curr.val
                l1Curr = l1Curr.next
            if l2Curr:
                val += l2Curr.val
                l2Curr = l2Curr.next
            
            carryover, res = divmod(val, counter * 10)
            curr.next = ListNode(res)
            curr = curr.next
        
        if carryover:
            curr.next = ListNode(carryover)
        
        return dummy.next





