class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        hasAlreadyRemovedCharacter = False
        def fn(l, r):
            nonlocal hasAlreadyRemovedCharacter
            while l < r:
                if s[l] != s[r]:
                    if hasAlreadyRemovedCharacter or not (s[l] == s[r - 1] or s[r] == s[l + 1]):
                        return False
                    hasAlreadyRemovedCharacter = True

                    leftDecision, rightDecision = False, False
                    if s[l] == s[r - 1]:
                        leftDecision = fn(l, r-1)
                    if s[r] == s[l + 1]:
                        rightDecision = fn(l + 1, r)
                    
                    return leftDecision or rightDecision
                l += 1
                r -= 1
            return True
        return fn(0, len(s) - 1)
        

