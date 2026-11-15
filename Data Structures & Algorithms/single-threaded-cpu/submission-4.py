class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        clock = 0
        res = []

        heap = []
        for i, task in enumerate(tasks):
            heapq.heappush(heap, (task[0], task[1], i))
        
        minProcessingTimeHeap = []

        while heap or minProcessingTimeHeap:

            # all tasks that can be processed during this tick
            while heap and clock >= heap[0][0]:
                _, processingTime, i = heapq.heappop(heap)
                heapq.heappush(minProcessingTimeHeap, (processingTime, i))
            
            if minProcessingTimeHeap:
                # least processing time consuming task
                processingTime, i = heapq.heappop(minProcessingTimeHeap)
                clock += processingTime
                res.append(i)
            else:
                clock = heap[0][0]
        
        return res
            



        # 1. get available tasks
        # 2. get shortest processing time
        # available_tasks = []