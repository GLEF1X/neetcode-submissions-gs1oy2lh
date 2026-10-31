# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        curr = root
        parent = None
        def findMaxNode(node: TreeNode, parent: TreeNode):
            if not node.right:
                return node, parent
            return findMaxNode(node.right, node)
        def findMinNode(node: TreeNode, parent: TreeNode):
            if not node.left:
                return node, parent
            return findMaxNode(node.left, node)

        while curr:
            ref = curr
            if key == curr.val:
                # leaf node
                if not (curr.right or curr.left):
                    if parent:
                        if parent.left and parent.left.val == curr.val:
                            parent.left = None
                            break
                        elif parent.right and parent.right.val == curr.val:
                            parent.right = None
                            break
                    else:
                        # the only node in the tree
                        return None
                
                maxNode, parentOfMaxNode = findMaxNode(curr.left, curr) if curr.left else findMinNode(curr.right, curr)
                curr.val = maxNode.val
                if parentOfMaxNode.left and parentOfMaxNode.left.val == maxNode.val:
                    parentOfMaxNode.left = None
                elif parentOfMaxNode.right and parentOfMaxNode.right.val == maxNode.val:
                    parentOfMaxNode.right = None


            elif key < curr.val:
                curr = curr.left
            else:
                curr = curr.right
            parent = ref
        
        return root