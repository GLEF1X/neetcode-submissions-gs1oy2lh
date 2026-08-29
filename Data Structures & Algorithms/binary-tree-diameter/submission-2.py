# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        # diameter = height(left) + height(right) + 1
        # max(height(left) + height(right) + 1)
        # f(node) = max(height(node.left) + height(node.right) + 1, maxDiameter)


        def getNodeHeight(node: Optional[TreeNode]) -> int:
            nonlocal diameter

            if not node:
                return 0
            
            leftHeight = getNodeHeight(node.left)
            rightHeight = getNodeHeight(node.right)
            # at node 2 height = 1
            # left--
            # at node 3(left child of 2) height = 2
            # at node 5(left child pf 3) height = 3
            # right--
            # the problem is that at node 2 left subtree responds height = 3, right responds height = 2
            # and the sum is 5

            diameter = max(
                leftHeight + rightHeight,
                diameter
            )

            return 1 + max(leftHeight, rightHeight)
        

        getNodeHeight(root)
        return diameter
        

