class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        curr = []
        usage = {i: 1 for i in range(len(nums))}

        def backtrack(i):
            if len(curr) == len(nums):
                res.add(tuple(curr.copy()))
                return
            
            for j in range(len(nums)):
                if usage[j] == 0:
                    continue

                num = nums[j]
                curr.append(nums[j])
                usage[j] = 0
                backtrack(i + 1)
                curr.pop()
                usage[j] = 1

        backtrack(0)
        return [list(item) for item in res]