class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        maxLen=0
        for r in range(len(nums)):
            if nums[r]==0:
                while l!=r+1:
                    l+=1
            maxLen=max(maxLen,r-l+1)
        return maxLen

        