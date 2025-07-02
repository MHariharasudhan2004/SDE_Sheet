class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        if len(nums)==1:
            return [nums[::]]
        if len(nums)==2:
            return [nums[::],nums[::-1]]
        for i in range(len(nums)):
            num=nums.pop(0)
            array=self.permute(nums)
            for a in array:
                a.append(num)
                res.append(a)
            nums.append(num)
        return res
        