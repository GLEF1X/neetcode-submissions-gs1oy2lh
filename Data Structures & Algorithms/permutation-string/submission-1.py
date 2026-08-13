class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s2 = lecabee, s1 = abc
        L, R = 0, len(s1) - 1
        s1FrequencyMap = [0] * 26
        currWindowFreqMap = [0] * 26

        getMapIdx = lambda asciiCode: ord(asciiCode) - ord('a')

        for char in s1:
            s1FrequencyMap[getMapIdx(char)] += 1 
        
        for i in range(min(len(s1), len(s2))):
            currWindowFreqMap[getMapIdx(s2[i])] += 1
        
        while R < len(s2):
            freqMapIdx = 0
            areEqual = True
            while freqMapIdx < 26:
                if s1FrequencyMap[freqMapIdx] != currWindowFreqMap[freqMapIdx]:
                    areEqual = False
                    break
                
                freqMapIdx += 1
            if areEqual:
                return True
            else:
                currWindowFreqMap[getMapIdx(s2[L])] -= 1
                L += 1
                R += 1
                if R < len(s2):
                    currWindowFreqMap[getMapIdx(s2[R])] += 1
            
        return False
            