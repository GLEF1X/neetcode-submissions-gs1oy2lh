# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isBalanced = True

        def getNodeHeight(node: Optional[TreeNode]) -> int:
            nonlocal isBalanced
            if not node:
                return 0
            
            leftHeight = getNodeHeight(node.left)
            rightHeight = getNodeHeight(node.right)
            if abs(rightHeight - leftHeight) > 1:
                isBalanced = False

            return 1 + max(leftHeight, rightHeight)

        
        getNodeHeight(root)
        return isBalanced
