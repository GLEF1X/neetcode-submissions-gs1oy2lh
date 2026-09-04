# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        queue = deque([root])
        while queue:
            l = len(queue)
            for i in range(l):
                currNode = queue.popleft()
                if not currNode:
                    continue
                if i == l - 1:
                    result.append(currNode.val)

                if currNode.left:
                    queue.append(currNode.left)
                if currNode.right:
                    queue.append(currNode.right)
        
        return result