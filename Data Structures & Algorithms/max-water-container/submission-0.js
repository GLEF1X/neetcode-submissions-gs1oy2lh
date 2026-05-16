class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let maxWaterAmount = 0;
        for (let i = 0; i < heights.length; i++) {
            for (let j = i+1; j < heights.length; j++) {
                const currentWaterAmount = (j - i) * Math.min(heights[j], heights[i])
                if (currentWaterAmount > maxWaterAmount) {
                    maxWaterAmount =  currentWaterAmount
                }
            }
        }

        return maxWaterAmount
    }
}
