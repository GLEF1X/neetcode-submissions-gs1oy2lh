class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        # -2,0,0,2,2
        # -4,-1,-1,0,1,2

        for i, num in enumerate(nums):
            if i >= 1 and num == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left < right:
                currSum = nums[left] + nums[right] + num
                if currSum == 0:
                    result.append([num, nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif currSum < 0: # we need bigger numbers
                    left += 1
                else: # we need smaller numbers
                    right -= 1
        
        # (-1,0,1), (-1,0,2), (-1,0,-1), (-1,0,-4)
        # (-1,1,2), (-1,1,-1), (-1,1,-4)
        # (-1,2,-1), (-1,-1,-4)
        # (0,1,2), (0,1,-1), (0,1,-4)
        # (1,2,-1), (1,2,-4)


        return result

        