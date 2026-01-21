class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1count={}
        window={}
        if len(s2)<len(s1):
            return False
        for i in s1:
            s1count[i]=1+s1count.get(i,0)
        k=len(s1)
        for j in range(k):
            window[s2[j]]=1+window.get(s2[j],0)
        if s1count==window:
            return True
        l=0
        for r in range(k,len(s2)):
            window[s2[l]]-=1
            if window[s2[l]]==0:
                window.pop(s2[l])
            window[s2[r]]=1+window.get(s2[r],0)
            if s1count==window:
                return True
            l+=1
            print(l)
            if l>=len(s2):
                break
        return False



