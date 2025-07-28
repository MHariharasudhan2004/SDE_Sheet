class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        MaxA=0
        stk=[]
        n=len(heights)
        for i,height in enumerate(heights):
            start=i
            while stk and height<stk[-1][0]:
                h,j=stk.pop()
                w=i-j
                a=h*w
                MaxA=max(MaxA,a)
                start=j
            stk.append((height,start))
        while stk:
            h,j=stk.pop()
            w=n-j
            a=w*h
            MaxA=max(a,MaxA)
        return MaxA


        