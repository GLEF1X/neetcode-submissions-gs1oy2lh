class Solution:
    def longestPalindrome(self, s: str) -> str:
        # subproblem def: P(i,j)= {
        #   True if dp[i:j] is a palindrome 
        #   False otherwise
        #}
        # recurrence relation: P(i,j) = {
        #   if s[i] == s[j]: return P(i+1, j-1)
        #   else: return False
        #}
        # topo order(suffix/prefix/substring): i = 0,...,n-1, j = n-1,...,0
        # base case: P(i, j) = {
        #   True if i == j
        #   
        #}
        # target: P(0)
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        
        for i in range(0, len(dp)):
            for j in range(0, len(dp[i])):
                if i == j:
                    dp[i][j] = True

        maxI, maxJ = 0, 1
        for i in range(n-1, -1, -1):
            for j in range(n-1, i,-1):
                if s[i] == s[j]:
                    if i == j - 1 and j == i + 1:
                        dp[i + 1][j - 1] = True
                    dp[i][j] = dp[i + 1][j - 1]
                    if dp[i][j]:
                        if j-i >= maxJ - maxI:
                            maxI, maxJ = i, j + 1
                else:
                    dp[i][j] = False
        
        return s[maxI:maxJ]


