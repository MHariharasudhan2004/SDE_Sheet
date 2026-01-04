class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        s={}
        l=0
        maxLen=0
        for r in range(len(fruits)):
            s[fruits[r]]=1+s.get(fruits[r],0)
            while len(s)>2:
                s[fruits[l]]-=1
                if s[fruits[l]]==0:
                    s.pop(fruits[l])
                l+=1
            maxLen=max(maxLen,r-l+1)
        return maxLen
        