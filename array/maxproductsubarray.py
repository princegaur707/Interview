class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mini=maxi=ans=nums[0]
        for i in range(1,len(nums)):
            n=nums[i]
            temp=maxi
            maxi=max(n,n*mini,n*maxi)
            mini=min(n,n*mini,n*temp)
            ans=max(ans,maxi)
        return ans