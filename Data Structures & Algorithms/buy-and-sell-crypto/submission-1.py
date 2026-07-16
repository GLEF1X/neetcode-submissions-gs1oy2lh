class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyingPrice = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            maxProfit = max(prices[i] - buyingPrice, maxProfit)
            buyingPrice = min(buyingPrice, prices[i])

        return maxProfit
