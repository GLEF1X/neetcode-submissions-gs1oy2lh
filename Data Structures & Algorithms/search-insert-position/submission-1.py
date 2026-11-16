class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            middle = l + (r - l) // 2
            probe = nums[middle]

            if probe == target:
                return middle
            elif probe > target:
                r = middle - 1
            else:
                l = middle + 1
        
        return l

