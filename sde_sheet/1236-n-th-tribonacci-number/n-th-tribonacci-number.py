class Solution:
    def tribonacci(self, n: int) -> int:
        dp=[0,1,1]
        if n<3:
            return dp[n]
        for i in range(3,n+1):
            dp[i%3]=sum(dp)
        return dp[n%3]