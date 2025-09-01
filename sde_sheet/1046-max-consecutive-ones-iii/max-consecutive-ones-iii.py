class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n=len(nums)
        l=0
        max_w=0
        max_zer=0
        for r in range(n):
            if nums[r]==0:
                max_zer+=1
            while max_zer>k:
                if nums[l]==0:
                    max_zer-=1
                l+=1
            max_w=max(max_w,r-l+1)
        return max_w
