class Solution:
    def numDecodings(self, s: str) -> int:
        ## suffixes
        # 1012
        # Subproblem definition:  D(i) = number of ways to decode an encoded string with prefix i, i+1, ..., n-1
        # Recurrence relation: D(i) = if s[i] == "0": 0 else D(i + 1) + D(i + 2)
        # base case(-s): D(n)=0, D(n+1)=0
        # target: D(0)
        # topological order: n, n-1, ..., 0
        n = len(s)
        dp = [0] * (n + 2)
        dp[n] = 1

        for i in range(n-1, -1, -1):
            if s[i] == "0":
                if i == 0:
                    return 0
                dp[i] = 0
            else:
                if i < n - 1 and (s[i] > "2" or (s[i + 1] > "6" and s[i] == "2")):
                    dp[i] = dp[i + 1]
                    continue

                dp[i] = dp[i + 1] + dp[i + 2]

        return dp[0]
