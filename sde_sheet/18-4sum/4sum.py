class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        quad=[]
        nums.sort()
        def KSum(k,start,target):
            if k!=2:
                for i in range(start,len(nums)-1):
                    if i>start and nums[i]==nums[i-1]:
                        continue
                    quad.append(nums[i])
                    KSum(k-1,i+1,target-nums[i])
                    quad.pop()
                return
            l,r=start,len(nums)-1
            while l<r:
                if nums[l]+nums[r]<target:
                    l+=1
                elif nums[l]+nums[r]>target:
                    r-=1
                else:
                    res.append(quad+[nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        KSum(4,0,target)
        return res


        