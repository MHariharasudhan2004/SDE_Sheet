class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        count=0
        el=0
        for i in range(n):
            if count==0:
                el=nums[i]
                count=1
            elif el==nums[i]:
                count+=1
            elif el!=nums[i]:
                count-=1
            
        cnt1=0
        for i in range(n):
            if nums[i]==el:
                cnt1+=1
        if cnt1>n//2:
            return el


        