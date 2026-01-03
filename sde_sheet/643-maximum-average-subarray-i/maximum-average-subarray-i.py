class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum1=0
        n=len(nums)
        sum1=sum(nums[:k])
        maxSum=sum1
        for i in range(k,n):
            sum1+=nums[i]
            sum1-=nums[i-k]
            maxSum=max(sum1,maxSum)
        return maxSum/k