class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[-1] = 1

        for i in range(n-2, -1, -1):
            temp = [lis for j, lis in enumerate(dp[i+1:],start=i+1) if nums[i] < nums[j]]
            dp[i] = 1 + (max(temp) if temp else 0)
        
        return max(dp)