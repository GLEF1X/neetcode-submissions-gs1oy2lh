# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level = []

            # flush out the entire level
            for _ in range(len(queue)):
                currNode = queue.popleft()
                level.append(currNode.val)
                if currNode.left:
                    queue.append(currNode.left)
                
                if currNode.right:
                    queue.append(currNode.right)
            
            result.append(level)
    
        return result


