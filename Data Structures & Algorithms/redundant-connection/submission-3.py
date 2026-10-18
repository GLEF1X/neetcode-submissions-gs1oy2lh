class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(1, len(edges) + 1)]

        def find_parent(vertex):
            if vertex == parent[vertex - 1]:
                return vertex
            
            parent[vertex - 1] = find_parent(parent[vertex - 1])
            return parent[vertex-1]

        
        def merge_sets(a, b):
            a = find_parent(a)
            b = find_parent(b)

            if a == b:
                return False
            
            parent[b - 1] = a
            return True
            
        
        for a,b in edges:
            if not merge_sets(a,b):
                return [a, b]
        
