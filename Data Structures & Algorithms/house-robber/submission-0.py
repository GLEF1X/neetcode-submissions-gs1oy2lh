class Solution:
    def rob(self, nums: List[int]) -> int:
        # B(i) = max amount that can robbed from houses i..n
        # original = B(0)
        # relate: B(i) = max(B(i + 2) + v[i]), B(i + 3) + v[i])
        # topo: i: n,n-1...0
        # [1]
        n = len(nums)
        dp = [0] * (n + 1)
        # [1,1,3,3]

        # [0, 0, 0, 3]
        # [0, 0, 3, 3]
        # [0, 4, 3, 3]
        # [4, 4, 3, 3]

        # [2,100,8,3,6]
        # [0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 6]
        # [0, 0, 0, 3, 6]
        # [0, 0, 14, 3, 6]
        # [16, 106, 14, 3, 6]

        for i in range(n-1, -1, -1):
            dp[i] = max(
                dp[i + 2] + nums[i] if i < n - 1 else nums[i],
                dp[i + 3] + nums[i] if i < n - 2 else nums[i]
            )
        
        return max(dp[0], dp[1])
