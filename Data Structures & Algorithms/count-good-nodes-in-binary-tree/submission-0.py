# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        countOfGoodNodes = 0

        def dfs(node: TreeNode, parentMaxNode: TreeNode):
            nonlocal countOfGoodNodes

            # TODO: think about a tree with only root node. In such case there's no good nodes per our code which
            # is not true
            if node.val >= parentMaxNode.val:
                countOfGoodNodes += 1

            
            newMaxParentNode = node if node.val > parentMaxNode.val else parentMaxNode
            if node.left:
                dfs(node.left, newMaxParentNode)
            if node.right:
                dfs(node.right, newMaxParentNode)
    
        dfs(root, root)
        return countOfGoodNodes