import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)

        while len(stones) >= 2:
            stone1 = heapq._heappop_max(stones)
            stone2 = heapq._heappop_max(stones)
            if stone1 == stone2:
                continue
            else:
                heapq._heappush_max(stones, stone1 - stone2)

        return stones[0] if stones else 0