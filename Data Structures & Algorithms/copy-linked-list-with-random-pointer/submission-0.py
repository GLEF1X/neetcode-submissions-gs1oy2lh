"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        tail = dummy
        curr = head
        randomNodeToDependents = {}

        while curr:
            # initialize depedents for a random node(that might not have been iterated on yet)
            if not randomNodeToDependents.get(curr.random):
                randomNodeToDependents[curr.random] = {
                    "dependents": [],
                    "newCopy": None
                }
            
            # if random node was previously initialized we retrieve it
            randomNode = randomNodeToDependents[curr.random]["newCopy"]

            copy = Node(curr.val, None, randomNode)
            # we haven't seen this node yet and it's not initialiezd
            if not randomNode:
                randomNodeToDependents[curr.random]["dependents"].append(copy)
            
            tail.next = copy
            # store random nodes:
            # for the similicity Node 5 -> [Node 7, Node 3]
            # when we are on node 5 we compare the nodes by identity and then on these nodes set the random pointer, clear the entry

            # does anyone depenend on us logic:
            if not randomNodeToDependents.get(curr):
                randomNodeToDependents[curr] = {
                    "dependents": [],
                    "newCopy": None
                }
            
            randomNodeToDependents[curr]["newCopy"] = copy

            for dependent in randomNodeToDependents[curr]["dependents"]:
                dependent.random = copy

            curr = curr.next
            tail = tail.next

        return dummy.next