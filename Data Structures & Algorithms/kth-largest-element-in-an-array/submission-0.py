class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            if len(heap) >= k:
                currMax = heap[0]
                if num > currMax:
                    heapq.heapreplace(heap, num)
            else:
                heapq.heappush(heap, num)
        
        return heap[0]
        
