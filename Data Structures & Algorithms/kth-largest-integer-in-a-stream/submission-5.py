from _heapq import heapify
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        self._heap = nums
        heapq.heapify(self._heap)

        while len(self._heap) > k:
            heapq.heappop(self._heap)

        

    def add(self, val: int) -> int:
        # heap is full
        if len(self._heap) >= self._k:
            # val greater than min
            if val > self._heap[0]:
                heapq.heappop(self._heap)
                heapq.heappush(self._heap, val)
        else:
            heapq.heappush(self._heap, val)

        return self._heap[-self._k]
        
