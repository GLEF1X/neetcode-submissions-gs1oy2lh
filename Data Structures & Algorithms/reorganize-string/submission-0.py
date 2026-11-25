class Solution:
    def reorganizeString(self, s: str) -> str:
        m = [0] * 26

        for char in s:
            m[ord(char) - ord('a')] += 1
        
        maxHeap = []

        for charRelativeIdx, freq in enumerate(m):
            if freq == 0:
                continue

            char = charRelativeIdx + ord('a')
            maxHeap.append((-freq, char))
        
        heapq.heapify(maxHeap)

        res = []
        while maxHeap:
            freq, char = heapq.heappop(maxHeap)
            freq = abs(freq)

            if res and ord(res[-1]) == char:
                if not maxHeap:
                    return ""

                prevFreq, prevChar = freq, char
                freq, char = heapq.heappop(maxHeap)
                freq = abs(freq)

                heapq.heappush(maxHeap, (-(prevFreq), prevChar))

            res.append(chr(char))
            
            if freq > 1:
                heapq.heappush(maxHeap, (-(freq - 1), char))
        
        return "".join(res)