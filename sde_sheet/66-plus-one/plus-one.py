class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        num=''
        for i in range(n):
            num+=str(digits[i])
        num=int(num)
        num+=1
        num=list(str(num))
        return list(map(int,num))

        