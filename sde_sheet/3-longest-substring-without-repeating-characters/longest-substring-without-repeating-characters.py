class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        setx=set()
        if len(s)==0:
            return 0
        n=len(s)
        max_w=0
        l=0
        for r in range(n):
            if s[r] in setx:
                while l<r and s[r] in setx:
                    setx.remove(s[l])
                    l+=1
            setx.add(s[r])
            max_w=max(max_w,r-l+1)
        return max_w
        