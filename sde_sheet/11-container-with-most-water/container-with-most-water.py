class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea=0
        l=0
        r=len(height)-1
        while l<r:
            h=min(height[l],height[r])
            w=r-l
            maxArea=max(maxArea,h*w)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxArea