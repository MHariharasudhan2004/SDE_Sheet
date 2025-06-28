class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        ds=[]
        def bactrack(ind,target):
            if ind==len(candidates):
                if target==0:
                    ans.append(ds[:])
                return
            if candidates[ind]<=target:
                ds.append(candidates[ind])
                bactrack(ind,target-candidates[ind])
                ds.pop()
            bactrack(ind+1,target)
        bactrack(0,target)
        return ans
        