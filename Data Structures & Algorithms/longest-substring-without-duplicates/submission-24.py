class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLongestSubstringLen = 0
        left = 0
        right = 0
        chars = {}

        for i in range(len(s)):
            if chars.get(s[i]):
                # Remove characters through the previous occurrence
                for j in range(left, right):
                    chars.pop(s[j])
                    left += 1

                    if s[j] == s[i]:
                        break
                    # zvdvf
                    continue

            # Do not continue; include the current character
            chars[s[i]] = True
            right += 1

            maxLongestSubstringLen = max(right - left, maxLongestSubstringLen)

        return maxLongestSubstringLen
