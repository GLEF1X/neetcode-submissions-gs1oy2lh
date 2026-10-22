class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        ptr = 0

        def search():
            nonlocal ptr
            firstStr = strs[0]
            firstStrLen = len(firstStr)
            while True:
                if ptr >= firstStrLen:
                    return
                char = firstStr[ptr]
                for i in range(1, len(strs)):
                    str_ = strs[i]
                    if ptr >= len(str_):
                        return
                    if str_[ptr] != char:
                        return
                
                ptr += 1
        search()
        
        return strs[0][0:ptr]



