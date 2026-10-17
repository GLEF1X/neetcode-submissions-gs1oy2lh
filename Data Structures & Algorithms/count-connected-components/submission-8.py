class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def find_set(vertex):
            if vertex == parent[vertex]:
                return vertex
            
            return find_set(parent[vertex])
        
        def merge_sets(a, b):
            a = find_set(a)
            b = find_set(b)

            if a != b:
                parent[b] = a
        
        for a,b in edges:
            merge_sets(a, b)
        
        res = set()
        for vertex in parent:
            res.add(find_set(vertex))
        
        return len(res)