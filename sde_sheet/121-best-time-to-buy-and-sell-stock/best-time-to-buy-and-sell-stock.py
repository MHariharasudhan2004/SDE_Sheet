class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro=0
        min_value=float('inf')
        for i in range(len(prices)):
            min_value=min(prices[i],min_value)
            maxPro=max(maxPro,prices[i]-min_value)
        return maxPro
        