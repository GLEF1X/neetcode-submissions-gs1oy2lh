class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacencyList = defaultdict(list)

        for edge in edges:
            adjacencyList[edge[0]].append(edge[1])
            adjacencyList[edge[1]].append(edge[0])
        
        visited = set()
        
        groups = 0
        def dfs(vertex):
            if vertex in visited:
                return False
            visited.add(vertex)

            neighbors = adjacencyList[vertex]
            if not neighbors:
                return True
                
            for neighbor in neighbors:
                dfs(neighbor)
            
            return True
        
        print(list(adjacencyList))
        for vertex in list(adjacencyList):
            if dfs(vertex):
                groups += 1

        
        return groups + (n - len(visited))
        

