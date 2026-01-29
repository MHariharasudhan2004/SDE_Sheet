class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        res=0
        while(l<=r):
            mid=l+(r-l)//2
            if nums[mid]<target:
                l=mid+1
                res=mid+1 #case 2
            elif nums[mid]>target:
                r=mid-1
               # res=mid+1 #case 3
                #res=mid-1 #case 4
            else:
               return mid
        return 0 if res<0 else res          
        