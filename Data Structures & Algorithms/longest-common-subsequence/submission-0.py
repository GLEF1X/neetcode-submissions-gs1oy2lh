class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Subproblem: L(i, j) = LCS(L[i:], L[j:])
        # Original problem: L(0, 0)
        # Recurrence relation: if s[i] == s[j]: return 1 + L(i + 1, j + 1)
        # return max(L(i + 1, j), L(i, j + 1))
        # Topological order: i=n,n-1,...0 |A| decreasing, j=k,k-1,...0 |B| decreasing
        # Base case(-s):

        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]


        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(
                        dp[i + 1][j],
                        dp[i][j+1]
                    )
        
        return dp[0][0]