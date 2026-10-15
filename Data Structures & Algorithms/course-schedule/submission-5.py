class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacencyMap = defaultdict(list)
        for pair in prerequisites:
            course, prereq = pair
            adjacencyMap[course].append(prereq)

        visited = set()
        inProgress = set()

        def dfs(vertex):
            if vertex in inProgress:
                return False
            if vertex in visited:
                return True

            visited.add(vertex)
            inProgress.add(vertex)
            for neighbor in adjacencyMap[vertex]:
                if not dfs(neighbor):
                    return False
            inProgress.remove(vertex)
            
            return True
        
        for vertex in list(adjacencyMap.keys()):
            if not dfs(vertex):
                return False
            inProgress.clear()
        
        return True