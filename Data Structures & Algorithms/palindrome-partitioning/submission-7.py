class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = set()
        cur = []
        cache = {}

        def isPalindrome(str_):
            if (isPalindromeCached := cache.get(str_)) is not None:
                return isPalindromeCached

            l, r = 0, len(str_) - 1
            while l <= r and str_[l] == str_[r]:
                l += 1
                r -= 1
            cache[str_] = l > r
            
            return l > r
        
        def backtrack(i):
            if i == len(s):
                # logic of determining whether it's a palindrome
                allSubstringsArePalindromes = True
                for subString in cur:
                    if not isPalindrome(subString):
                        allSubstringsArePalindromes = False
                        break
                if allSubstringsArePalindromes:
                    result.add(tuple(cur.copy()))
                return
            
            if not cur or isPalindrome(cur[-1]):
                cur.append(s[i])
                backtrack(i + 1)
                cur.pop()
            
            prev = ""
            if len(cur):
                prev = cur[-1]
                cur[-1] = prev + s[i]
                backtrack(i + 1)
                cur[-1] = prev

        backtrack(0)
        return [list(subArr) for subArr in result]