class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        numOfRows = len(matrix)
        numOfColumns = len(matrix[0])
        right = numOfRows * numOfColumns - 1

        if numOfColumns == 1 and numOfRows == 1:
            return matrix[0][0] == target

        while left <= right:
            middleIdx = left + (math.trunc((right - left) / 2)) # is 2
            row = middleIdx // numOfColumns
            col = middleIdx % numOfColumns
            probeNum = matrix[row][col]
            
            if probeNum == target:
                return True
            elif target < probeNum:
                right = middleIdx - 1
            else:
                left = middleIdx + 1
        return False