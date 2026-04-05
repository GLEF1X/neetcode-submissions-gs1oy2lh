class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {
        const openParanthesis = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        const stack = []

        for (let char of s) {
            if (openParanthesis[char]) {
                stack.push(char)
                continue
            }

            const lastOpenParenthese = stack.pop()
            const correspondingClose = openParanthesis[lastOpenParenthese]
            if (correspondingClose !== char) {
                return false
            }
        }

        return stack.length === 0
    }
}
