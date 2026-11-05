class Solution:
    def countSubstrings(self, s: str) -> int:
        # Subproblem: P(i, j) = 
        # Original problem:
        # Recurrence relation
        # Topological order:
        # Base case
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        palindromeCount = 0
        for i in range(n):
            for j in range(n):
                if i == j:
                    palindromeCount += 1
                    dp[i][j] = True
        
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == j:
                    continue
                if s[i] != s[j]:
                    dp[i][j] = dp[j][i] = False
                else:
                    if abs(j - i) > 1:
                        dp[i][j] = dp[j][i] = dp[min(i,j)+1][max(i,j)-1]
                    else:
                        dp[i][j] = dp[j][i] = True
                    
                    if j >= i and dp[i][j]:
                        palindromeCount += 1
        
        return palindromeCount
                
        