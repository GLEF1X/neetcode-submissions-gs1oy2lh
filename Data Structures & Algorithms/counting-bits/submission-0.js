class Solution {
    /**
     * @param {number} n
     * @return {number[]}
     */
    countBits(n) {
        const res = []
        for (let i = 0; i <= n; i++) {
            let [temp, count] = [i, 0];
            while (temp !== 0) {
                temp &= (temp - 1);
                count++;
            }
            res.push(count)
        }
        return res
    }
}
