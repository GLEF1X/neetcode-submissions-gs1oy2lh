class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # zxyzxyz

        maxLongestSubstringLen = 0
        left = 0
        right = 0
        chars = {}

        # dvdf - failing with left = right

        # dvdvf
        # pwwkew

        for i in range(len(s)):
            if chars.get(s[i]):
                for j in range(left, right):
                    chars.pop(s[j])
                    left += 1
                    if s[j] == s[i]:
                        break
                
            
            right += 1 # right = 1, left = 0 i = 0 | i = 2, right = 2, left = 1
            maxLongestSubstringLen = max(right - left, maxLongestSubstringLen)
            chars[s[i]] = True

        return maxLongestSubstringLen
            
            