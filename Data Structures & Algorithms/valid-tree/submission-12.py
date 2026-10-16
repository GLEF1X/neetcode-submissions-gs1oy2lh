class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1 and not edges:
            return True

        if n - 1 != len(edges):
            return False
        
        adjacencyList = defaultdict(list)
        for a, b in edges:
            adjacencyList[a].append(b)
            adjacencyList[b].append(a)
        
        initial = []
        if adjacencyList:
            initial.append(list(adjacencyList.keys())[0])
        
        visited = set(initial)
        queue = deque(initial)
        while queue:
            currVertex = queue.popleft()            

            for neighbor in adjacencyList[currVertex]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append(neighbor)

        
        return len(visited) == n