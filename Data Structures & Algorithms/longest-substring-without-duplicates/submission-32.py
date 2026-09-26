class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # zxyxxyz

        l, r = 0, 0
        longestSubstringLength = 0
        chars = set()
        while r < len(s):
            if s[r] in chars:
                # shrink the window
                # we don't know where exactly this duplicated symbol is at, we only now it's in a substring
                while s[l] != s[r]:
                    chars.remove(s[l])
                    l += 1
                l += 1

            chars.add(s[r])
            longestSubstringLength = max(longestSubstringLength, r - l + 1)
            r += 1
        
        return longestSubstringLength
            
