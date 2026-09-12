class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        # max depth = log2(2^len(nums))=len(nums)
        def backtrack(depth):
            if depth >= len(nums):
                res.append(subset[:])
                return
            
            # branch where we decide to add a number to a subset
            subset.append(nums[depth])
            backtrack(depth + 1)

            subset.pop()
            backtrack(depth + 1)


        backtrack(0)
        return res