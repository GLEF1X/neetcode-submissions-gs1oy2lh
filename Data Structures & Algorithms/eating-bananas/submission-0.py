class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles) - 1
        
        # [1,4,3,2], h = 9
        # [1,2,3,4]
        # 1) idx = 4 - 1 = 3 // 2 = 1, rate = 1 + 1 = 2 -> 6 hours
        # idx = 1 -> 10 hours
        minEatingRate = 0
        while left <= right:
            middleIdx = left + ((right - left) // 2)
            eatingRatePerHour = middleIdx + 1

            numberOfHoursRequiredToEatAllBananasInPile = 0
            for numberOfBananasInPile in piles:
                numberOfHoursRequiredToEatAllBananasInPile += math.ceil(numberOfBananasInPile / eatingRatePerHour)
            
            if numberOfHoursRequiredToEatAllBananasInPile <= h:
                minEatingRate = eatingRatePerHour
                right = middleIdx - 1
            else:
                left = middleIdx + 1

        return minEatingRate

        