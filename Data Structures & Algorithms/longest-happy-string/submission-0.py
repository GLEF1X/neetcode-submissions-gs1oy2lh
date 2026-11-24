class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = [(-a, "a"), (-b, "b"), (-c, "c")]
        heapq.heapify(maxHeap)

        res = []

        while maxHeap:
            occurences, char = heapq.heappop(maxHeap)
            occurences = abs(occurences)

            if occurences < 1:
                continue
            
            if len(res) >= 2 and res[-1] == char and res[-2] == char:
                if not maxHeap:
                    return ""
                
                if abs(maxHeap[0][0]) < 1:
                    return "".join(res)
                
                prevOccur, prevChar = occurences, char
                occurences, char = heapq.heappop(maxHeap)
                occurences = abs(occurences)
                # preserve not selected char
                heapq.heappush(maxHeap, (-prevOccur, prevChar))



                
            res.append(char)
            heapq.heappush(maxHeap, (-(occurences - 1), char))

        return "".join(res)