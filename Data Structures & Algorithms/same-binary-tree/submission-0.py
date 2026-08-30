# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [p, q]

        while stack:
            pNode, qNode = stack.pop(), stack.pop()
            if pNode == qNode: # both are None case
                continue
            if pNode is None or qNode is None:
                return False
            
            if pNode.val != qNode.val:
                return False
            
            stack.extend([pNode.left, qNode.left, pNode.right, qNode.right])
        
        return True
