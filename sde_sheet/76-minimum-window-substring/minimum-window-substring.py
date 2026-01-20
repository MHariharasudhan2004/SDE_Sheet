class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="": return ""
        scount={}
        tcount={}
        for i in range(len(t)):
            tcount[t[i]]=1+tcount.get(t[i],0)
        have,need=0,len(tcount)
        res,resLen=[-1,-1],float("infinity")
        l=0
        for r in range(len(s)):
            c=s[r]
            scount[c]=scount.get(c,0)+1

            if c in tcount and scount[c]==tcount[c]:
                have+=1

            while have==need:
                if r-l+1<resLen:
                    res=[l,r]
                    resLen=r-l+1
                scount[s[l]]-=1
                if s[l] in tcount and scount[s[l]]<tcount[s[l]]:
                    have-=1
                l+=1
        l,r=res
                
        return s[l:r+1] if resLen!=float("infinity") else ""

