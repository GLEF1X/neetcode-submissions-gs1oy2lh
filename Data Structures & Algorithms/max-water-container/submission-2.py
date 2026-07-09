class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftPtr = 0
        rightPtr = len(heights) - 1
        maxArea = 0

        while leftPtr <= rightPtr:
            width = rightPtr - leftPtr
            height = width * min(heights[leftPtr], heights[rightPtr])
            maxArea = max(maxArea, height)

            if heights[leftPtr] < heights[rightPtr]:
                leftPtr += 1
            elif heights[leftPtr] == heights[rightPtr]:
                leftPtr += 1
                rightPtr -= 1
            else:
                rightPtr -= 1
        
        return maxArea