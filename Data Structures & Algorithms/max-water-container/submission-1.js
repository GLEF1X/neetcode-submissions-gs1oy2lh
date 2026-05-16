class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let [leftPtr, rightPtr] = [0, heights.length - 1];

        let maxArea = 0;
        while (leftPtr < rightPtr) {
            maxArea = Math.max(
                (rightPtr - leftPtr) * Math.min(heights[leftPtr], heights[rightPtr]),
                maxArea,
            );
            if (heights[leftPtr] < heights[rightPtr]) {
                leftPtr++
            } else if (heights[rightPtr] < heights[leftPtr]) {
                rightPtr--
            } else {
                leftPtr++
                rightPtr--
            }
        }

        return maxArea;
    }
}
