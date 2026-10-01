class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        numberOfParens = n
        result = set()
        currStrParts = []
        
        def backtrack(i):
            nonlocal currStrParts
            if len(currStrParts) == n * 2:
                if isValidStr(currStrParts):
                    result.add("".join(currStrParts))
                return
            
            currStrParts.append("(")
            backtrack(i + 1)

            currStrParts.pop()
            currStrParts.append(")")
            backtrack(i + 1)
            currStrParts.pop()
        
        def isValidStr(s):
             count = 0
             for paren in s:
                 if paren == "(":
                     count += 1
                 elif paren == ")":
                     if count <= 0:
                         return False
                     count -= 1
             return count == 0 
        

        backtrack(0)
        return list(result)
            