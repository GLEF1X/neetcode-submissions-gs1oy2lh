# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 1->2->8
        # 4->9->1

        # 5->1->4

        # 1->9->9->9->9...->9
        # 4->9->9->9->9...->9

        # 5->8->9->9->9

        # [9,9,9,9,9,9,9]
        # [9,9,9,9]

        # 8(1)->9(1)->9(1)->9(1)->9

        l1Node = l1
        l2Node = l2
        carryover = 0
        resultingList = ListNode(0)
        curr = resultingList

        while l1Node or l2Node:
            nodeSum = (l1Node.val if l1Node else 0) + (l2Node.val if l2Node else 0) + carryover
            if nodeSum >= 10:
                nodeSum -= 10
                carryover = 1
            else:
                carryover = 0
            

            curr.next = ListNode(nodeSum)
            curr = curr.next

            if l1Node:
                l1Node = l1Node.next
            if l2Node:
                l2Node = l2Node.next
        
        if carryover:
            curr.next = ListNode(carryover)
        
        return resultingList.next




