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

        m = defaultdict(list)
        stack = deque([(root, 0)])

        while stack:
            currNode, currLvl = stack.popleft()

            m[currLvl].append(currNode.val)

            if currNode.left:
                stack.append((currNode.left, currLvl + 1))
            
            if currNode.right:
                stack.append((currNode.right, currLvl + 1))
        
        result = [v for v in m.values()]
        
        return result


