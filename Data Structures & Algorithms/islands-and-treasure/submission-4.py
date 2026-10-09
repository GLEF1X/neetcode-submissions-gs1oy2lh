class Solution:
    LAND_SENTINEL = 2**31 - 1

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:   
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    continue
                queue.append((i, j, 0))

                
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        while queue:
            entryRowIdx, entryColIdx, distance = queue.popleft()
            if visited[entryRowIdx][entryColIdx]:
                continue
            visited[entryRowIdx][entryColIdx] = True

            if grid[entryRowIdx][entryColIdx] == -1:
                continue

            # either land or visited but still need to see if it's a minimum really
            if grid[entryRowIdx][entryColIdx] != -1 and grid[entryRowIdx][entryColIdx] != 0:
                grid[entryRowIdx][entryColIdx] = min(distance, grid[entryRowIdx][entryColIdx])
                    
            for neighborRowIdx, neighborColIdx in (
                (entryRowIdx + 1, entryColIdx), (entryRowIdx - 1, entryColIdx), (entryRowIdx, entryColIdx + 1), (entryRowIdx, entryColIdx - 1)
            ):
                if not (0 <= neighborRowIdx < len(grid)) or not (0 <= neighborColIdx < len(grid[0])):
                    continue
                queue.append((neighborRowIdx, neighborColIdx, distance + 1))
                    



                    