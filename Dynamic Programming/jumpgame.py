# https://leetcode.com/problems/jump-game/
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastidx = len(nums)-1
        for i in range(lastidx,-1,-1):
            if i + nums[i] >= lastidx:
                lastidx = i
        return lastidx == 0
