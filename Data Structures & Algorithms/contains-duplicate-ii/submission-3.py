class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
       left, right = 0, 0
       m = {}

       # 1,3,3,1,1, k = 2
       # nums=[1,2,2,3]
       # k=3
       
       for i in range(len(nums)):
            if left != right and nums[left] == nums[right]:
                return True
            if sameNumIdx := m.get(nums[i]):
                if i - sameNumIdx <= k:
                    return True

                
            
            if right - left >= k:
                left += 1
            right += 1
            m[nums[i]] = i

       return False
                
 
