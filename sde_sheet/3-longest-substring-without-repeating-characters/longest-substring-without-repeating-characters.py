class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        scount=set()
        maxLen=0
        l=r=0
        while r<len(s):
            if s[r] not in scount:
                scount.add(s[r])
                maxLen=max(maxLen,r-l+1)
            else:
                while s[r] in scount:
                    scount.remove(s[l])
                    l+=1
                scount.add(s[r])
            r+=1
        return maxLen



        