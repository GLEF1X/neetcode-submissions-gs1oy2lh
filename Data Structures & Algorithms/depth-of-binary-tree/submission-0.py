# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxDepth = 0
        def getDepth(node: TreeNode, currDepth = 1):
            nonlocal maxDepth
            maxDepth = max(currDepth, maxDepth)
            if node.left:
                getDepth(node.left, currDepth + 1)
            if node.right:
                getDepth(node.right, currDepth + 1)
        
        if root:
            getDepth(root)

        return maxDepth