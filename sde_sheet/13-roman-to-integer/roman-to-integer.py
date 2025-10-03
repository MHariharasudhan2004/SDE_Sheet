class Solution:
    def romanToInt(self, s: str) -> int:
        sym={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        res=0
        for i in range(len(s)-1):
            if sym[s[i]]<sym[s[i+1]]:
                res-=sym[s[i]]
            else:
                res+=sym[s[i]]
        return res+sym[s[-1]]
        