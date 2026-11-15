class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        minLen = float("inf")
        windowSum = 0

        for R in range(len(nums)):
            windowSum += nums[R]
            while windowSum >= target and L <= R:
                minLen = min(minLen, R - L + 1)
                windowSum -= nums[L]
                L += 1
        
        if isinstance(minLen, float):
            return 0

        return minLen