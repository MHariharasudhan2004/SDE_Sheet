class Solution:
    def numOfWays(self, n: int) -> int:
        c3=6
        c2=6
        mod=1e9+7
        for i in range(2,n+1):
            temp=c3
            c3=(2*c2+2*c3)%mod
            c2=(2*temp+3*c2)%mod
        return int((c3+c2)%mod)
        