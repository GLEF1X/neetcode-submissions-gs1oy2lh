# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        
        stack = [root]
        while stack:
            currNode = stack.pop()
            
            if val > currNode.val:
                if currNode.right:
                    stack.append(currNode.right)
                else:
                    currNode.right = TreeNode(val)
            else:
                if currNode.left:
                    stack.append(currNode.left)
                else:
                    currNode.left = TreeNode(val)
        
        return root
            

            

        
