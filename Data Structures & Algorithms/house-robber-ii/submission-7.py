class Solution:
    def rob(self, nums: List[int]) -> int:
        # base case: b(n)=0
        # rel: B(i) = max(B(i + 2) + v[i], B(i + 3) + v[i])
        # first part:
        # if i == 0 and n % 2 == 1: B(i + 2) + v[i] - v[n]
        # elif i ==0 and n % 2 == 0: B(i + 2) + v[i]
        # second part:
        # if i == 0 and n % 2 == 1: B(i + 2) + v[i] - v[n]
        # elif i ==0 and n % 2 == 0: B(i + 2) + v[i]
        # topo: i=n,n-1,...0
        # target: max(b(0), b(1))

        # 3,4,3
        # [0,0,0,0]
        # [0,0,3]
        # [3,4,3]
        
        # [2,9,8,3,6]
        # [0, 0, 0 ,0 ,0 ]
        # [0, 0, 0, 0, 6]
        # [0, 0, 14, 3, 6]
        # case 1 - [16, 15, 14, 3, 6]
        # case 2 - [16, 15, 14, 3]
        # case 3 - [16, 15, 14, 3, 6,7]
        # case 4 - [16, 15, 14, 3, 6, 7, 8]

        # if n = 3, dp_size = 3 + 1 = 4, i < 1
        # [1,2,3]

        # [1,2,3]
        # [0, 0, 0, 0]
        # [0, 2, 3]
        # [1, 2, 3]

        # 5,1,2,6,12,7,9,3,4,10
        # [0,0,0,0,0,0,0,0,0,0,0]
        # [38,32,33,26,31,20,19,13,4,10,0]

        # rob first house ^(xor) rob last house 
        n = len(nums)
        dp = [0] * (n + 1)

        for i in range(n-1, 0, -1): # don't include first
            dp[i] = max(
                dp[i + 2] + nums[i] if i < n-2 else nums[i],
                dp[i + 3] + nums[i] if i < n-3 else nums[i]
            )
        maxWithoutIncludingFirst = max(dp)
        
        dp = [0] * (n + 1)
        for i in range(n-2, -1, -1): # don't include last
            dp[i] = max(
                dp[i + 2] + nums[i] if i < n-2 else nums[i],
                dp[i + 3] + nums[i] if i < n-3 else nums[i]
            )
        
        return max(*dp, maxWithoutIncludingFirst, nums[0])

