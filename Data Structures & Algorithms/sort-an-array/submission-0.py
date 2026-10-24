class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 5,10,2,1,3
        # 1,2,3,5,10
        # left = 0
        # right = 4
        if len(nums) <= 1:
            return nums

        middle = len(nums) // 2

        return self.merge(self.sortArray(nums[:middle]), self.sortArray(nums[middle:]))
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        l, r = 0, 0
        result = []

        while l < len(left) and r < len(right):
            leftElement, rightElement = left[l], right[r]
            if leftElement > rightElement:
                result.append(rightElement)
                r += 1
            elif leftElement < rightElement:
                result.append(leftElement)        
                l += 1
            else:
                result.extend([leftElement, rightElement])
                l += 1
                r += 1
        
        for i in range(l, len(left)):
            result.append(left[i])
        for j in range(r, len(right)):
            result.append(right[j])

        return result
        