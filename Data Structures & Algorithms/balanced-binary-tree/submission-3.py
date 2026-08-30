# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getNodeHeight(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            leftHeight = getNodeHeight(node.left)
            rightHeight = getNodeHeight(node.right)

            if (leftHeight == -1 or rightHeight == -1) or abs(rightHeight - leftHeight) > 1:
                return -1

            return 1 + max(leftHeight, rightHeight)

        
        return getNodeHeight(root) != -1
