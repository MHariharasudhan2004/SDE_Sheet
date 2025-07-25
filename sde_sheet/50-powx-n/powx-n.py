class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n==0:
            return 1
        if n<0:
            x=1/x
            n=-n
        half=self.myPow(x,n//2)
        if n%2:
            return x*half*half
        else:
            return half*half
        