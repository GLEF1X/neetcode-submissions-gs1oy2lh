class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        # [10,1,5]

        for i in range(0, len(prices)):
            for j in range(i, len(prices)):
                maxProfit = max(prices[j] - prices[i], maxProfit)

        return maxProfit
            
