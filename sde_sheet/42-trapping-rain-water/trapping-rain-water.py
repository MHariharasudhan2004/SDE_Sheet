class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        left=0
        right=len(height)-1
        leftMax=0
        rightMax=0
        res=0
        while left<right:
            if height[left]<=height[right]:
                if height[left]>leftMax:
                    leftMax=height[left]
                else:
                    res+=leftMax-height[left]
                left+=1
            else:
                if height[right]>leftMax:
                    leftMax=height[right]
                else:
                    res+=leftMax-height[right]
                right-=1
        return res
        