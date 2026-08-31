# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        while stack:
            currNode = stack.pop()

            subrootStack = [(currNode, subRoot)]
            isSubtree = True
            while subrootStack:
                mainTreeNode, subRootNode = subrootStack.pop()

                if mainTreeNode == subRootNode: # None case
                    continue
                
                if mainTreeNode is None or subRootNode is None:
                    isSubtree = False
                    break

                if mainTreeNode.val != subRootNode.val:
                    isSubtree = False
                    break
                
                subrootStack.append((mainTreeNode.left, subRootNode.left))
                subrootStack.append((mainTreeNode.right, subRootNode.right))
            
            if isSubtree:
                return True
            
            if currNode.left:
                stack.append(currNode.left)
            if currNode.right:
                stack.append(currNode.right)
        
        return False