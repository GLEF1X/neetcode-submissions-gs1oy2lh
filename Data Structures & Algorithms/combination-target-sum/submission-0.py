class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        addends, currSum = [], 0

        def inner(i):
            nonlocal currSum
            if currSum == target:
                result.append(addends.copy())
                return
            elif currSum > target:
                return

            for j in range(i, len(nums)):
                num = nums[j]
                addends.append(num)
                currSum += num

                inner(j)

                addends.pop()
                currSum -= num

        
        inner(0)
        return result