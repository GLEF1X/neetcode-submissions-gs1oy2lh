import heapq

class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for x, y in points:
            distance = x**2 + y**2

            if len(distances) >= k:
                maxDistance = abs(distances[0][0])
                if distance < maxDistance:
                    heapq.heapreplace(distances, (-distance, x, y))
            else:
                heapq.heappush(distances, (-distance, x, y))

        return [[x, y] for _, x, y in distances]

