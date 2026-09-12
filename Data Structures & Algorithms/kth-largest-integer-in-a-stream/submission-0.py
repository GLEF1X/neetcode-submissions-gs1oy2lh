import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self._k = k
        self._heap = nums
        heapq._heapify_max(self._heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self._heap, val)
        return heapq.nlargest(self._k, self._heap)[-1]
        
