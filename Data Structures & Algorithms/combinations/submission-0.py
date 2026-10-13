class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        cur = []

        def backtrack(i):
            if len(cur) == k:
                res.append(cur.copy())
                return

            for j in range(i, n):
                num = j + 1
                cur.append(num)
                backtrack(num)
                cur.pop()
        
        backtrack(0)
        return res