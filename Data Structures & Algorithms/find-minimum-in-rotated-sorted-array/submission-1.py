class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minElement = nums[0]
        lastEl = nums[-1]
        # 1 2 3 4 5 6
        # 2 2 2 2 2 2
        # if an element is not the last number and it it is greater than the last element
        # then it's a rotated portion

        while left <= right:
            middleIdx = left + ((right - left) // 2)
            probe = nums[middleIdx]            
            isNumberInTail = middleIdx != len(nums) - 1 and probe > lastEl

            minElement = min(minElement, nums[middleIdx])

            if isNumberInTail:
                left = middleIdx + 1
            else:
                if nums[middleIdx - 1] > nums[middleIdx]:
                    # our prev element is the end of rotation
                    return minElement
                right = middleIdx - 1

            # if middleIdx < len(nums) and nums[middleIdx + 1] > nums[middleIdx]:
            #     left = middleIdx + 1
            #     minElement = min(minElement, nums[middleIdx])
            # elif nums[middleIdx] > nums[middleIdx - 1]:

        return minElement
