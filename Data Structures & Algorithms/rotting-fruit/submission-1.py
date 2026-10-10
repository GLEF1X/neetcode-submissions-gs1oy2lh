class Solution:
    EMPTY_CELL_MARKER = 0
    FRESH_FRUIT_MARKER = 1
    ROTTEN_FRUIT_MARKER = 2
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != self.ROTTEN_FRUIT_MARKER:
                    continue
                queue.append((i, j, 0))
        
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        maxTick = 0
        while queue:
            i, j, tick = queue.popleft()
            if visited[i][j]:
                continue
            maxTick = max(tick, maxTick)
            visited[i][j] = True

            if grid[i][j] == self.FRESH_FRUIT_MARKER:
                grid[i][j] = self.ROTTEN_FRUIT_MARKER
            
            for neighborRowIdx, neighborColIdx in (
                (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)
            ):
                if not (0 <= neighborRowIdx < len(grid)) or not (0 <= neighborColIdx < len(grid[0])):
                    continue
                # it was cared for in initial sweep for BFS
                val = grid[neighborRowIdx][neighborColIdx]
                if val == self.ROTTEN_FRUIT_MARKER or val == self.EMPTY_CELL_MARKER:
                    continue
                
                # empty cells still could be visited, there's no problem with that

                queue.append((neighborRowIdx, neighborColIdx, tick + 1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        
        return maxTick
            





