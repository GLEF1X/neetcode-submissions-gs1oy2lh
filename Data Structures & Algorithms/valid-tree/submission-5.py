class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n - 1 != len(edges):
            return False
        
        adjacencyList = defaultdict(list)
        for a, b in edges:
            adjacencyList[a].append(b)
            adjacencyList[b].append(a)
        
        visited = set()
        inProgress = {}

        def dfs(vertex, clock = 0):
            inProgressClock = inProgress.get(vertex, clock)
            if clock - inProgressClock > 1:
                return False
            if vertex in visited:
                return True
            
            inProgress[vertex] = clock
            for neighbor in adjacencyList[vertex]:
                if (neighborInProgressClock := inProgress.get(neighbor)) is not None:
                    if clock - neighborInProgressClock <= 1:
                        continue

                if not dfs(neighbor, clock + 1):
                    return False
            del inProgress[vertex]
            visited.add(vertex)

            return True

        
        for vertex in list(adjacencyList.keys()):
            if not dfs(vertex):
                return False
        
        return True