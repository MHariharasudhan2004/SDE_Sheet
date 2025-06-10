class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m=defaultdict(int)
        n=len(nums)
        ans=[]
        for num in nums:
            m[num]+=1
        for key,value in m.items():
            if value>n//3:
                ans.append(key)
        return ans
