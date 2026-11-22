class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacencyList = defaultdict(list)

        for edge in times:
            source, target, time = edge

            adjacencyList[source].append((target, time))
        
        visited = set()
        heap = [(0, k)]
        res = {v: float("inf") for v in range(1, n+1)}
        res[k] = 0

        while heap:
            pathDelay, vertex = heapq.heappop(heap)

            for edge in adjacencyList[vertex]:
                if edge in visited:
                    continue

                targetVertex, edgeDelay = edge
                totalDelay = pathDelay + edgeDelay
                if res.get(targetVertex) is None:
                    res[targetVertex] = totalDelay
                
                res[targetVertex] = min(totalDelay, res[targetVertex])

                heapq.heappush(heap, (totalDelay, targetVertex))
                visited.add(edge)

        for vertex in range(1, n+1):
            if vertex == k:
                continue
            if vertex not in res:
                return -1
        
        res = max(res.values())
        if res == float("inf"):
            return -1
        
        return res