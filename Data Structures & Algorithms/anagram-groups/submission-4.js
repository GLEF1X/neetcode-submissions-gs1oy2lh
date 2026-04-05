class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const res = []        
        const map = {}
        for (const word of strs) {
            const matchArr = Array.from({ length: 26 }, () => 0)
            for (const char of word) {
                matchArr[char.charCodeAt(0) - 97]++
            }
            if (!map[matchArr]) {
                map[matchArr] = []
            }
            map[matchArr].push(word)
        }

        for (const element of Object.values(map)) {
            res.push(element)
        }
        return res
    }
}
