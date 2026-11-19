class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minAmountOfCoins = float("inf")
        memo = {}
        coins.sort()

        def recurse(i, coinSum = 0, amountOfCoins = 0):
            nonlocal minAmountOfCoins

            fewestAmountOfCoins = memo.get((i, coinSum))
            if fewestAmountOfCoins is not None and amountOfCoins >= fewestAmountOfCoins:
                return
            memo[(i, coinSum)] = min(fewestAmountOfCoins, amountOfCoins) if fewestAmountOfCoins is not None else amountOfCoins


            if coinSum == amount:
                minAmountOfCoins = min(minAmountOfCoins, amountOfCoins)
                return
            elif coinSum > amount:
                return
            if i < 0:
                return
            if amountOfCoins > minAmountOfCoins:
                return

            maxAmountOfCoins, remainder = divmod(amount - coinSum, coins[i])
            if remainder != 0:
                maxAmountOfCoins += 1
            if amountOfCoins + maxAmountOfCoins >= minAmountOfCoins:
                return

            for j in range(((amount - coinSum) // coins[i]), -1, -1):
                recurse(i - 1, coinSum + coins[i] * j, amountOfCoins + j)
        
        recurse(len(coins) - 1)

        return -1 if minAmountOfCoins == float("inf") else minAmountOfCoins
