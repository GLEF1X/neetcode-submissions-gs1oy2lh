class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        # 1 2 3 4 5 6
        # 2 2 2 2 2 2
        # if an element is not the last number and it it is greater than the last element
        # then it's a rotated portion
        # 3,4,5,6,7,8,1,2
        # target is 1

        # 3,4,5,6,7,8,1,2
        # target is 7

        # 5,1,3
        # target is 5

        # 5,1,2,3,4
        # target = 1
        # [1,2,3,4,5,6,7] k = 3 -> [5,6,7,1,2,3,4]
        # 1. reverse(origArray) -> [7,6,5,4,3,2,1] = reversedArray
        # 2. [*reverse(reversedArray[0:k]), *reverse(reversedArray[k:])]

        # 5,1,2,3,4
        # target = 1

        # 1,2,3,4,5
        # target = 1

        # 4,5,6,7,2,3, target = 1
        
        # 3,4,5,6,0,1,2
        # target = 4

        while left <= right:
            middle = left + ((right - left) // 2)
            probe = nums[middle]

            if nums[middle] == target:
                return middle

            # Left half is sorted
            if nums[left] <= nums[middle]:
                # Target is inside the sorted left half
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1

            # Right half is sorted
            else:
                # Target is inside the sorted right half
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1
            

        return -1
