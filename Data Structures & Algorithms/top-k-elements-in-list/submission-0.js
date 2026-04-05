class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const freqMap = {}
        for (const num of nums) {
            freqMap[num] = (freqMap[num] ?? 0) + 1
        }
        // [_, 1, 2, 3]
        // [5, 3, 5, 3, 4, 5, 2, 2]
        // {5: 3, 4: 1, 3: 2}
        // [4, 1]
        const bucketFreq = []
        for (const [num, freq] of Object.entries(freqMap)) {
            const bucket = bucketFreq[freq] ?? []
            bucket.push(num)
            bucketFreq[freq] = bucket
        }
        // [3: [5], 1:[4], 2:[3, 2]]
        // [1,2,3]

        let res = []
        for (let i = bucketFreq.length - 1; i >= 0 && res.length < k; i--) {
            if (bucketFreq[i]) {
                res.push(...bucketFreq[i])
            }
        }


        return res
    }
}
