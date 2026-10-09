class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def dfs(rowIdx, colIdx):
            visited[rowIdx][colIdx] = True

            area = 1
            for neighborRowIdx, neighborColIdx in ((rowIdx + 1, colIdx), (rowIdx - 1, colIdx), (rowIdx, colIdx - 1), (rowIdx, colIdx + 1)):
                if not (0 <= neighborRowIdx < len(grid)):
                    continue
                if not (0 <= neighborColIdx < len(grid[0])):
                    continue
                if grid[neighborRowIdx][neighborColIdx] == 0:
                    continue
                if visited[neighborRowIdx][neighborColIdx]:
                    continue
                
                area += dfs(neighborRowIdx, neighborColIdx)
            
            return area

        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or visited[i][j]:
                    continue
                maxArea = max(maxArea, dfs(i, j))
        return maxArea