class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        # [-1,0,2,4,6,8]
        # [-1,0,4,6,8]
        while left <= right:
            middle = left + ((right - left) // 2)

            probe = nums[middle]
            if probe == target:
                return middle
            elif probe > target:
                right = middle - 1
            else:
                left = middle + 1
        
        return -1
