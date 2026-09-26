class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []

        def backtrack(level = 0, excluded = set()):
            if level >= len(nums):
                result.append(curr.copy())
                return

            if nums[level] not in excluded:
                curr.append(nums[level])
                backtrack(level + 1, excluded)
                curr.pop()
            
            new = excluded.copy()
            new.add(nums[level])
            backtrack(level + 1, new)
        
        backtrack(0)
        return result