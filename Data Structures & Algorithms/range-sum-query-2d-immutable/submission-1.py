class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [
            row.copy() for row in matrix
        ]
        for rowIdx in range(len(self.prefix)):
            for colIdx in range(len(self.prefix[rowIdx])):
                self.prefix[rowIdx][colIdx] += (self.prefix[rowIdx][colIdx - 1] if colIdx >= 1 else 0) + (self.prefix[rowIdx - 1][colIdx] if rowIdx >= 1 else 0) - (self.prefix[rowIdx - 1][colIdx - 1] if rowIdx >= 1 and colIdx >= 1  else 0)
        print(self.prefix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2][col2] - (self.prefix[row2][col1 - 1] if col1 >= 1 else 0) - (self.prefix[row1 - 1][col2] if row1 >= 1 else 0) + (self.prefix[row1 - 1][col1 -1] if row1 >= 1 and col1 >= 1 else 0)


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)