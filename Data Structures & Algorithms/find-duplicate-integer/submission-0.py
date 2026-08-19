class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        duplicate = 0

        for bit in range(32):
            mask = 1 << bit

            nums_count = 0
            normal_count = 0

            for x in nums:
                if x & mask:
                    nums_count += 1

            for x in range(1, n + 1):
                if x & mask:
                    normal_count += 1

            if nums_count > normal_count:
                duplicate |= mask

        return duplicate