class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=float('inf')
        maxi=0
        for i in range(len(prices)):
            mini=min(mini,prices[i])            #finds the current minimum in current location or last minimum
            maxi=max(maxi,prices[i]-mini)       #finds the highest profit currently
        return maxi