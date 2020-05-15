# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx = 0
        mn = float('inf')
        for i in range(0,len(prices)):
            mn = min(mn,prices[i])
            mx = max(mx,prices[i]-mn)
        return mx
