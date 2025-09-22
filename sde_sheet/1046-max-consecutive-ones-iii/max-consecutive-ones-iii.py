class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_w=0
        num_zeros=0
        l=0
        n=len(nums)
        max_c=-1
        for r in range(n):
            if nums[r]==0:
                num_zeros+=1

            while num_zeros>k:
                if nums[l]==0:
                    num_zeros-=1
                l+=1
            max_w=r-l+1
            max_c=max(max_w,max_c)
        return max_c
        