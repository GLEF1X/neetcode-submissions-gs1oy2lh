class Solution {
    /**
     * @param {number} n - a positive integer
     * @return {number}
     */
    hammingWeight(n) {
        let res = 0;
        // 00000000000000000000000000001011
        // 0
        // 1011
        // 0001

        // 0101
        // 0001

        for (let i = 0; i < 32; i++) {
            const currentVal = n & (1<<i)
            if (currentVal !== 0 ) {
                res++
            }
        }

        return res
    }
}
