class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const numsMapping = {}

        for (const num of nums) {
            const count = numsMapping[num]
            if (!count) {
                numsMapping[num] = 1    
            } else {
                return true
            }
        }

        return false
    }
}
