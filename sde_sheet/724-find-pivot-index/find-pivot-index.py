class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixsum=0
        total=sum(nums)
        for i in range(len(nums)):
            rightsum=total-nums[i]-prefixsum
            if rightsum==prefixsum:
                return i
            prefixsum+=nums[i]
        return -1
        