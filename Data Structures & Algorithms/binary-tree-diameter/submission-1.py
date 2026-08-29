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

        def getNodeHeight(node: Optional[TreeNode], height: int = 0) -> int:
            if node is None:
                return height
            
            leftHeight = getNodeHeight(node.left, height + 1)
            rightHeight = getNodeHeight(node.right, height + 1)

            return max(leftHeight, rightHeight)

        deq = deque([root])

        while deq:
            currNode = deq.pop()

            diameter = max(
                getNodeHeight(currNode.left) + getNodeHeight(currNode.right),
                diameter
            )

            if currNode.left:
                deq.append(currNode.left)
            if currNode.right:
                deq.append(currNode.right)


        return diameter
        

