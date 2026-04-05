class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const seen = {}

        for (let i = 0; i < nums.length; i++) {
            const num = nums[i]
            const secondNumIdx = seen[target - num]
            if (secondNumIdx !== undefined) {
                return [i, secondNumIdx]
            }

            seen[num] = i
        }

        return []
    }
}
