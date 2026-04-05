class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const res = []
        while (strs.length) {
            const word = strs.shift()
            if (word === undefined) continue
            const innerRes = [word]

            const currentWordMap = {}
            for (const char of word) {
                currentWordMap[char] = (currentWordMap[char] ?? 0) + 1
            }

            for (let i = 0; i < strs.length; i++) {     
                const str = strs[i]
                if (str === undefined) continue              
                const innerWordStrMap = {}
                for (const char of str) {
                    innerWordStrMap[char] = (innerWordStrMap[char] ?? 0) + 1
                }

                let isAnagram = Object.keys(innerWordStrMap).length === Object.keys(currentWordMap).length
                for (const [char, freq] of Object.entries(currentWordMap)) {
                    const innerWordStrFreq = innerWordStrMap[char]
                    if (innerWordStrFreq !== freq) {
                        isAnagram = false
                    }
                }



                if (isAnagram) {
                    innerRes.push(str)
                    strs[i] = undefined
                }
            }
            res.push(innerRes)
        }

        return res
    }
}
