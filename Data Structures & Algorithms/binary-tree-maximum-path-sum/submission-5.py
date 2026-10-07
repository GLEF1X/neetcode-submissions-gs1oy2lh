# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")
        def dfs(node):
            nonlocal maxSum

            if not node:
                return 0

            leftMax, rightMax = 0, 0
            if node.left:
                leftMax = dfs(node.left)
            if node.right:
                rightMax = dfs(node.right)
            
            maxSum = max(max(leftMax, 0) + max(rightMax, 0) + node.val, maxSum, node.val)
            
            return max(leftMax, rightMax, 0) + node.val

        maxSum = max(dfs(root), maxSum)
        return maxSum
