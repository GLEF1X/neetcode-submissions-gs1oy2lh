# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        currList1Element = list1
        currList2Element = list2
        mergedList: Optional[ListNode] = None
        if not currList1Element or not currList2Element:
            if currList1Element:
                mergedList = currList1Element
                currList1Element = currList1Element.next
            elif currList2Element:
                mergedList = currList2Element
                currList2Element = currList2Element.next
        else:
            if currList1Element.val < currList2Element.val:
                mergedList = currList1Element
                currList1Element = currList1Element.next
            elif currList2Element.val < currList1Element.val:
                mergedList = currList2Element
                currList2Element = currList2Element.next
            else:
                mergedList = currList1Element
                currList1Element = currList1Element.next
        if not mergedList:
            return None
        head = mergedList

        while currList1Element or currList2Element:
            if not currList1Element and currList2Element:
                # exhausted first list
                mergedList.next = ListNode(currList2Element.val)
                mergedList = mergedList.next
                currList2Element = currList2Element.next if currList2Element else None
            elif not currList2Element and currList1Element:
                # exhausted second list
                mergedList.next = ListNode(currList1Element.val)
                mergedList = mergedList.next
                currList1Element = currList1Element.next if currList1Element else None
            elif currList1Element and currList2Element:
                if currList1Element.val == currList2Element.val:
                    mergedList.next = ListNode(currList1Element.val, ListNode(currList1Element.val))
                    mergedList = mergedList.next.next
                    currList1Element = currList1Element.next
                    currList2Element = currList2Element.next
                    continue
                minVal = min(currList1Element.val, currList2Element.val)
                if minVal == currList1Element.val:
                    mergedList.next = ListNode(currList1Element.val)
                    mergedList = mergedList.next
                    currList1Element = currList1Element.next if currList1Element else None
                else:
                    mergedList.next = ListNode(currList2Element.val)
                    mergedList = mergedList.next
                    currList2Element = currList2Element.next if currList2Element else None
        return head

            
            

