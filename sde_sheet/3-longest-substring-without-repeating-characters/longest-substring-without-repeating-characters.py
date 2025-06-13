class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        maxl=0
        charIndex=[-1]*128
        left=0
        for right in range(n):
            if charIndex[ord(s[right])]>=left:
                left=charIndex[ord(s[right])]+1
            charIndex[ord(s[right])]=right
            maxl=max(maxl,right-left+1)
        return maxl
        