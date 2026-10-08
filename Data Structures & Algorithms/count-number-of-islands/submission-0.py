class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()

        def dfs(rowIdx, colIdx):
            visited.add((rowIdx, colIdx))

            if grid[rowIdx][colIdx] == "0":
                return

            for neighborRowIdx, neighborColIdx in ((rowIdx, colIdx + 1), (rowIdx, colIdx - 1), (rowIdx + 1, colIdx), (rowIdx - 1, colIdx)):
                if neighborRowIdx < 0 or neighborRowIdx >= len(grid):
                    continue
                if neighborColIdx < 0 or neighborColIdx >= len(grid[0]):
                    continue
                if (neighborRowIdx, neighborColIdx) in visited:
                    continue
                
                dfs(neighborRowIdx, neighborColIdx)


    
        numberOfIslands = 0
        for rowIdx in range(len(grid)):
            for colIdx in range(len(grid[0])):
                if grid[rowIdx][colIdx] == "0" or (rowIdx, colIdx) in visited:
                    continue
                dfs(rowIdx, colIdx)
                numberOfIslands += 1
        
        return numberOfIslands