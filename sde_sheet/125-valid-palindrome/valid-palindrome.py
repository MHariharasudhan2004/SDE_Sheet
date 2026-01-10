class Solution:
    import re
    def isPalindrome(self, s: str) -> bool:
        r=re.sub(r'[^a-zA-Z0-9]',"",s)
        h=r.lower()
        return h[: : -1]==h[:]
        