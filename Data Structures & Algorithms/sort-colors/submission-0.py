class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2,1,0
        # 1,2,0
        # j = 2
        # 1,0,2

        for i in range(1, len(nums)):
            prevNum = nums[i - 1]
            num = nums[i]
            if num < prevNum:
                # need to swap
                j = i
                while j >= 1 and nums[j] < nums[j - 1]:
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
                    j -= 1
        



