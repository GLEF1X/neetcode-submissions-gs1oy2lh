class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def computeNumOfWays(n):
            if memoized := memo.get(n):
                return memoized
            
            if n <= 0:
                if n == 0:
                    return 1 
                return 0


            res = computeNumOfWays(n -1) + computeNumOfWays(n - 2)
            memo[n] = res
            return res

        return computeNumOfWays(n)