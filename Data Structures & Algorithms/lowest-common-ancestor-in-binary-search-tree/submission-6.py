# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]

        while stack:
            currNode = stack.pop()
            if min(p.val, q.val) < currNode.val < max(q.val, p.val):
                return currNode

            # Covers: the ancestor is allowed to be a descendant of itself.
            if currNode == p or currNode == q:
                return currNode
            
            # Since currNode is neither target nor between their values,
            # p and q must both lie in the same subtree.
            if p.val < currNode.val and currNode.left: # in the left subtree
                stack.append(currNode.left)
            elif p.val > currNode.val and currNode.right:
                stack.append(currNode.right)
        
        # dummy case, should always return in the loop
        return stack[-1]
            
                

