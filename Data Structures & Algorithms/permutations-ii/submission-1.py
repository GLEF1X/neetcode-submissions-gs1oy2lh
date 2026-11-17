class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []
        availability = Counter()

        for num in nums:
            availability[num] += 1

        def backtrack():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for num in availability.keys():
                if availability[num] <= 0:
                    continue

                curr.append(num)
                availability[num] -= 1
                backtrack()
                curr.pop()
                availability[num] += 1

        backtrack()
        return res