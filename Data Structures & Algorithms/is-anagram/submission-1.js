class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        const a = {}

        if (s.length !== t.length) {
            return false
        }

        for (const t of s) {
           a[t] ??= 0;
           a[t]++;
        }
        for (const t2 of t) {
            if (!a[t2]) {
                return false
            }
            a[t2]--
        }
        return true
    }
}
