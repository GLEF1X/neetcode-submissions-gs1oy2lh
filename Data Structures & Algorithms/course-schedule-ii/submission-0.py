class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjacencyList = {course: [] for course in range(numCourses)}

        for course, prereq in prerequisites:
            adjacencyList[course].append(prereq)
        
        visited = set()
        inProgress = set()
        result = []

        def dfs(vertex):
            if vertex in inProgress:
                return False
            if vertex in visited:
                return True
            visited.add(vertex)
            
            inProgress.add(vertex)
            for neighbor in adjacencyList[vertex]:
                if not dfs(neighbor):
                    return False
            inProgress.remove(vertex)
            result.append(vertex)
            return True

        
        for vertex in list(adjacencyList.keys()):
            if not dfs(vertex):
                return []
        
        return result