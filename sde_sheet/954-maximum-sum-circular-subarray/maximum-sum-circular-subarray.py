class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max=curr_min=0
        max_sum=float('-inf')
        min_sum=float('inf')
        tSum=0
        for n in nums:
            tSum+=n
            curr_max=max(curr_max+n,n)
            max_sum=max(max_sum,curr_max)
            
            curr_min=min(curr_min+n,n)
            min_sum=min(min_sum,curr_min)

        if max_sum<0:
            return max_sum
        return max(max_sum,tSum-min_sum)
        