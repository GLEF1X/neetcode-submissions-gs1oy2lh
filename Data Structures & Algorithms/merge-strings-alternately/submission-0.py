class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1Ptr, w2Ptr = 0, 0
        chars = []

        while w1Ptr < len(word1) or w2Ptr < len(word2):
            if w1Ptr < len(word1):
                chars.append(word1[w1Ptr])
                w1Ptr += 1
            if w2Ptr < len(word2):
                chars.append(word2[w2Ptr])
                w2Ptr += 1

        return "".join(chars)
