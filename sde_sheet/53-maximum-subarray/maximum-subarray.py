import sys
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=0
        maxi=-sys.maxsize-1
        for i in range(len(nums)):
            sum+=nums[i]
            if sum>maxi:
                maxi=sum
            if sum<0:
                sum=0
        return maxi