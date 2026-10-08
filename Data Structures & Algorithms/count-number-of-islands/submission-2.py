class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        cols = len(grid[0])
        rows = len(grid)
        visited = [[False] * cols for _ in range(rows)]

        def dfs(rowIdx, colIdx):
            if grid[rowIdx][colIdx] == "0":
                return
            visited[rowIdx][colIdx] = True

            for neighborRowIdx, neighborColIdx in ((rowIdx, colIdx + 1), (rowIdx, colIdx - 1), (rowIdx + 1, colIdx), (rowIdx - 1, colIdx)):
                if neighborRowIdx < 0 or neighborRowIdx >= rows:
                    continue
                if neighborColIdx < 0 or neighborColIdx >= cols:
                    continue
                if visited[neighborRowIdx][neighborColIdx]:
                    continue
                
                dfs(neighborRowIdx, neighborColIdx)


    
        numberOfIslands = 0
        for rowIdx in range(rows):
            for colIdx in range(cols):
                if grid[rowIdx][colIdx] == "0" or visited[rowIdx][colIdx]:
                    continue
                dfs(rowIdx, colIdx)
                numberOfIslands += 1
        
        return numberOfIslands