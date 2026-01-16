class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        currProd=1
        l=0
        subLen=0
        if k<=1:
            return 0
        for r in range(len(nums)):
            currProd*=nums[r]
            while currProd>=k:
                currProd=currProd//nums[l]
                l+=1

            subLen+=(r-l+1)
        return subLen

        