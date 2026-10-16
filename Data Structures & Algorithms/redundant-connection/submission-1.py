class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjacencyList = defaultdict(list)

        def isReachable(*, initialVertex, target):
            queue = deque([initialVertex])
            visited = set()
            while queue:
                currVertex = queue.popleft()
                if currVertex == target:
                    return True

                for neighbor in adjacencyList[currVertex]:
                    if neighbor in visited:
                        continue

                    queue.append(neighbor)
                    visited.add(neighbor)
            
            return False
        
        for a, b in edges:
            if isReachable(initialVertex=a, target=b):
                return [a,b]
            
            adjacencyList[a].append(b)
            adjacencyList[b].append(a)
        

