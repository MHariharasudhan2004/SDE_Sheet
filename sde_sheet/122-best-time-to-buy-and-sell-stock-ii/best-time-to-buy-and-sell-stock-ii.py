class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0
        i=0
        while i<n-1:
            #buy
            while i<n-1 and prices[i]>prices[i+1]:
                i+=1
            lo=prices[i]

            while i<n-1 and prices[i]<=prices[i+1]:
                i+=1
            hi=prices[i]
            profit+=hi-lo
        return profit
            
        