class Solution {
    /**
     * @param {string[]} strs
     * @returns {string}
     */
    encode(strs) {
        let result = ""
        for (const str of strs) {
            result += `${str.length}#${str}`
        }

        return result
    }

    /**
     * @param {string} str
     * @returns {string[]}
     */
    decode(str) {
        // 5#Hello5#World
        let res = []
        let currentLen = "", i = 0;
        while (i < str.length) {
            const char = str[i]
            if (!isNaN(char)) {
                currentLen += char
                i++
            } else if (char == "#") {
                const fullLength = parseInt(currentLen)
                res.push(str.slice(i+1, i+1+fullLength))
                i += fullLength + 1
                currentLen = ""
            }
        }
        return res
    }
}
