class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st=0
        n=len(s)
        if n==0:
            return 0
        charset=set()
        maxl=float("-inf")
        for i in range(n):
            if s[i] in charset:
                while st<i and s[i] in charset:
                    charset.remove(s[st])
                    st+=1
            charset.add(s[i])
            maxl=max(maxl,i-st+1)
        return maxl

        