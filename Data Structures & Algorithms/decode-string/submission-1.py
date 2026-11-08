class Solution:
    def decodeString(self, s: str) -> str:     
        def inner(start):
            nonlocal s

            i = start
            res = ""
            digits = ""
            numOfStrings = None
            while i < len(s):
                char = s[i]
                if not char.isdigit() and digits:
                    numOfStrings = int(digits)
                    digits = ""

                if char.isdigit():
                    digits += char
                elif char == "[":
                    innerStr, endPos = inner(i + 1)
                    if numOfStrings:
                        res += numOfStrings * innerStr
                    else:
                        res += innerStr
                    numOfStrings = None
                    i = endPos
                elif char == "]":
                    return res, i
                else:
                    # regular character
                    res += char
                i += 1
            
            return res, i
        
        decoded, _ = inner(0)
        return decoded

