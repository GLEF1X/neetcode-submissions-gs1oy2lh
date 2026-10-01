class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        numberOfParens = n
        result = set()
        currStrParts = []
        
        def backtrack(*, open_count, close_count):
            nonlocal currStrParts
            if len(currStrParts) == n * 2:
                if isValidStr(currStrParts):
                    result.add("".join(currStrParts))
                return
            
            # invalid branch
            if close_count > n or open_count > n:
                return 
            
            currStrParts.append("(")
            backtrack(open_count=open_count + 1, close_count=close_count)

            currStrParts.pop()
            currStrParts.append(")")
            backtrack(open_count=open_count, close_count=close_count + 1)
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
        

        backtrack(open_count=0, close_count=0)
        return list(result)
            