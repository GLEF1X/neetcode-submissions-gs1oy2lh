"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        oldToNewMap = {}
        visited = set()
        queue = deque([node])
        rootNode = None

        while queue:
            vertex = queue.popleft()
            if vertex in visited:
                continue
            visited.add(vertex)

            newVertex = oldToNewMap.get(vertex)
            if not newVertex:
                newVertex = Node(vertex.val)
                oldToNewMap[vertex] = newVertex

            if not rootNode:
                rootNode = newVertex

            for neighbor in vertex.neighbors:
                node = oldToNewMap.get(neighbor)
                if not node:
                    node = Node(neighbor.val)
                    oldToNewMap[neighbor] = node
                
                newVertex.neighbors.append(node)

                # 1. neighbotd node has already been created -> reuse
                # 2. otherwise, create new
                queue.append(neighbor)
        
        return rootNode
            
