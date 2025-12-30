class Solution:
    def trap(self, height: List[int]) -> int:
       
        l_wall=r_wall=0
        n=len(height)
        L=[0]*n
        R=[0]*n
        for i in range(n):
            j=-i-1
            L[i]=l_wall
            R[j]=r_wall
            l_wall=max(height[i],l_wall)
            r_wall=max(height[j],r_wall)
        res=0
        for i in range(n):
            s=min(L[i],R[i])
            res+=max(0,s-height[i])
        return res
