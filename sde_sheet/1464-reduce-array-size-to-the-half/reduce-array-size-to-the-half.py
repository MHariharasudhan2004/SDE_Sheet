class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        co=Counter(arr)
        values=sorted(co.values(),reverse=True)
        n=len(arr)
        rem=n//2
        removed=0
        for cou in values:
            rem-=cou
            removed+=1
            if rem<=0:
                return removed
        return removed       