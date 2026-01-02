class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        m=len(nums)
        n=m//2
        hashtable={}
        for i in nums:
            hashtable[i]=1+hashtable.get(i,0)
        for k,v in hashtable.items():
            if v==n:
                return k
        return -1

        