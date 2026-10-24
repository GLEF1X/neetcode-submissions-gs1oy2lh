class Solution:
    def minCostClimbingStairs(self, costs: List[int]) -> int:
        end = len(costs) - 1
        memo = {}

        def climb(i):
            if memoized := memo.get(i):
                return memoized

            if i > end:
                return 0
            
            min_ = costs[i] + min(climb(i + 1), climb(i + 2))
            memo[i] = min_
            return min_


        return min(climb(0), climb(1))
        
        