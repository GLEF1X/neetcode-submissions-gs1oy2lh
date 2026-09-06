# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(
            node: Optional[TreeNode],
            minParent=float("-inf"),
            maxParent=float("inf")
        ):
            if not node:
                return True

            if not (minParent < node.val < maxParent):
                return False

            return (
                isValid(node.left, minParent, node.val)
                and isValid(node.right, node.val, maxParent)
            )

        return isValid(root)
            
            
                