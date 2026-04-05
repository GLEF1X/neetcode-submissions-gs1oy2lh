class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        const res = []
        for (let i = 0; i < nums.length; i++) {
            let localRes
            for (let j = 0; j < nums.length; j++ ) {
                if (i == j) {
                    continue
                }
                if (localRes === undefined) {
                    localRes = nums[j]
                } else {    
                    localRes *= nums[j]
                }
            }
            res.push(localRes)
        }
        return res
    }
}
