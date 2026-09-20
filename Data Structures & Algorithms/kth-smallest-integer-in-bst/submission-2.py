# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfsInOrder(node: Optional[TreeNode]):
            if not node:
                return
            if len(arr) == k:
                return

            dfsInOrder(node.left)
            arr.append(node.val)
            dfsInOrder(node.right)
        
        dfsInOrder(root)

        return arr[k-1]



            
            