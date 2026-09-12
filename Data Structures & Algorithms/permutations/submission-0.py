class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        cur = []
        def backtrack(i):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            for j in range(len(nums)):
                if nums[j] in cur:
                    continue
                cur.append(nums[j])
                backtrack(i + 1)
                cur.pop()
        
        backtrack(0)
        return res