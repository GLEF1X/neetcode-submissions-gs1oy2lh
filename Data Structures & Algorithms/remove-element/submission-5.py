class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        endIdx = len(nums) - 1
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                continue
            if i < endIdx:
                while i < endIdx < len(nums) and nums[endIdx] == val:
                    endIdx -= 1
                print(i, endIdx)
                if i == endIdx:
                    print("here")
                    count += 1
                    continue
                nums[i], nums[endIdx] = nums[endIdx], nums[i]
            else:
                count += 1
        
        return len(nums) - count