class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        if n==1:
            return nums[0]
        while i<n-1:
            if nums[i]!=nums[i+1]:
                return nums[i]
            i+=2 
        return nums[-1]