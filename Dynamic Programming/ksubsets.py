# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k:
            return False
        sm = sum(nums)
        if sm % k != 0:
            return False
        nums.sort(reverse=True)
        target = [sm/k]*k
    
        def dfs(pos):
            if pos == len(nums):
                return True
            for i in range(k):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(pos+1):
                        return True
                    target[i] += nums[pos] 
            return False
        return  dfs(0)
                
