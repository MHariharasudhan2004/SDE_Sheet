class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftsum=0
        total=sum(nums)
        for i in range(len(nums)):
            rightsum=total-nums[i]-leftsum
            if rightsum==leftsum:
                return i
            leftsum+=nums[i]
        return -1
        