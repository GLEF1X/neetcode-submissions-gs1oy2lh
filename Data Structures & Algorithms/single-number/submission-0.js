class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    singleNumber(nums) {
        // 011
        // 011
        // 010
 
        // 010<- OR  010 <-AND 010 <- XOR
        // 011       011       011 
        // 011       010       001

        let x = 0
        for (const num of nums) {
            x ^= num
        }
        return x
    }
}
