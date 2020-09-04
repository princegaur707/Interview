class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp=nums
        for i in range(1,len(nums)):
            if dp[i-1]>0:
                dp[i]+=dp[i-1]
        return max(dp)
        