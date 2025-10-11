class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        sign=1
        res=0
        if s=="":
            return 0
        if s[0]=='-' or s[0]=="+":
            sign=1-2*(s[0]=='-')
            s=s[1:]
        for char in s:
            if not char.isdigit():
                break
            else:
                res=res*10+int(char)
        res=sign*res
        if res>2**31-1:
            return 2**31-1
        elif res<-2**31:
            return -2**31
        return res

