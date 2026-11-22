class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjacencyList = defaultdict(list)

        for edge in times:
            source, target, time = edge

            adjacencyList[source].append((target, time))
        
        visited = set()
        heap = [(0, k)]
        dist = {v: float("inf") for v in range(1, n+1)}
        dist[k] = 0

        while heap:
            pathDelay, vertex = heapq.heappop(heap)

            for edge in adjacencyList[vertex]:
                targetVertex, edgeDelay = edge

                if edgeDelay > dist[targetVertex]:
                    continue
                totalDelay = pathDelay + edgeDelay
                if totalDelay < dist[targetVertex]:
                    if dist.get(targetVertex) is None:
                        dist[targetVertex] = totalDelay
                
                    dist[targetVertex] = min(totalDelay, dist[targetVertex])
                    heapq.heappush(heap, (totalDelay, targetVertex))
                visited.add(edge)

        res = max(dist.values())
        if res == float("inf"):
            return -1
        
        return res