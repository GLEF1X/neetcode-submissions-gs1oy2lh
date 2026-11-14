class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
       m = {}
       for i in range(len(nums)):
            if (sameNumIdx := m.get(nums[i])) is not None:
                if i - sameNumIdx <= k:
                    return True
            
            m[nums[i]] = i

       return False
                
 
