class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        ds=[]
        candidates.sort()
        def backtrack(ind,target):
            if target==0:
                ans.append(ds[:])
                return
            for i in range(ind,len(candidates)):
                if i>ind and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>target:
                    break
                ds.append(candidates[i])
                backtrack(i+1,target-candidates[i])
                ds.pop()
        backtrack(0,target)
        return ans

        