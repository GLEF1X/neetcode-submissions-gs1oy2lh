class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def inner(n):
            if n == 0:
                return 0
            elif n == 1 or n == 2:
                return 1
            
            if cached := memo.get(n):
                return cached
            
            res = inner(n - 3) + inner(n - 2) + inner(n - 1)
            memo[n] = res
            return res
        return inner(n)
        # n = 5
        # n=3 -> 2
        # f(5) = f(2) + f(3) + f(4)
        # f(2) = 1
        # f(3) = 0 + 1 + 1 = 2
        # f(4) = f(1) + f(2) + f(3) = 1 + 1 + 2 = 4
        