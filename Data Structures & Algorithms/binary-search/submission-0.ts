class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums: number[], target: number): number {
        let left = 0,
            right = nums.length - 1;

        while (left <= right) {
            const middleIdx = left + Math.trunc((right - left) / 2);
            const currentNum = nums[middleIdx];
            if (currentNum === target) {
                return middleIdx;
            } else if (target < currentNum) {
                // discard right side
                right = middleIdx - 1;
            } else {
                // discard left side because target > currentNum
                left = middleIdx + 1;
            }
        }

        return -1;
    }
}
