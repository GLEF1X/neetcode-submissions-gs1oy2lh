class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLongestSubstringLen = 0
        left = 0
        right = 0
        chars = set()

        for i in range(len(s)):
            if s[i] in chars:
                # Remove characters through the previous occurrence
                for j in range(left, right):
                    chars.discard(s[j])
                    left += 1

                    if s[j] == s[i]:
                        break

            # Do not continue; include the current character
            chars.add(s[i])
            right += 1

            maxLongestSubstringLen = max(right - left, maxLongestSubstringLen)

        return maxLongestSubstringLen
