class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        m = [0] * 26
        longestSubstringLen = 0

        # XYYX

        while right < len(s):
            char = s[right]
            indexToStore = ord(char) - 65
            m[indexToStore] += 1

            windowLen = right - left + 1
            mostFrequentCharOccurencesNum = 0
            for value in m:
                mostFrequentCharOccurencesNum = max(value, mostFrequentCharOccurencesNum) if value else mostFrequentCharOccurencesNum
            
            numberOfReplacementsRequiredToMaintainValidSubstring = windowLen - mostFrequentCharOccurencesNum
            if numberOfReplacementsRequiredToMaintainValidSubstring <= k:
                longestSubstringLen = max(longestSubstringLen, windowLen)
            else:
                m[ord(s[left]) - 65] -= 1
                left += 1
            
            right += 1
            
        return longestSubstringLen