# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # [0, 1, 2, 3, 4, 5, 6]
        # start at linked list len 
        # [0, 6, 1] -> 6
        # curr = "first" element(at the start)
        # temp = curr.next
        # curr.next = tail
        # tail.next = temp
        # [0,6,1,2,3,4,5] -> result

        # [0,6,1,5,2,3,4] -> after 5
        # [0,6,1,5,2,4]

        deq = []
        curr = head
        while curr:
            deq.append(curr)
            curr = curr.next
            
        middleIdx = len(deq) // 2
        currStartIdx = 0
        while len(deq) - 1 > middleIdx:
            tail = deq.pop() # 8
            curr = deq[currStartIdx] # 2
            temp = curr.next # 4
            curr.next = tail # 2 -> 8
            tail.next = temp # 8 -> 4
            currStartIdx += 1
        
        deq[-1].next = None
        


