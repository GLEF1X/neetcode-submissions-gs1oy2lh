import heapq

class Solution:
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __lt__(self, other):
            return self.x**2 + self.y**2 < other.x**2 + other.y**2

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for x, y in points:
            heapq.heappush(distances, self.Point(x, y))

        result = []

        for _ in range(k):
            p = heapq.heappop(distances)
            result.append([p.x, p.y])

        return result

