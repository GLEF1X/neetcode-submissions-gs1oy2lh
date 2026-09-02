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

            if (currNode.left == p and currNode.right == q) or (currNode.right == p and currNode.left == q):
                return currNode
            
            if (currNode == p and (currNode.left == q or currNode.right == q)) or (currNode == q and (currNode.left == p or currNode.right == p)):
                return currNode
            
            if p.val < currNode.val < q.val or q.val < currNode.val < p.val:
                return currNode
            
            if (currNode == p) or (currNode == q):
                return currNode
            
            if p.val < currNode.val and currNode.left: # in the left subtree
                stack.append(currNode.left)
            elif p.val > currNode.val and currNode.right:
                stack.append(currNode.right)
        
        return stack[-1]
            
                

