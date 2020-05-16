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
