class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s=len(grid)
        n=s*s
        S=n*(n+1)//2
        P=n*(n+1)*(2*n+1)//6
        S1,P1=0,0
        for i in range(s):
            for j in range(s):
                S1+=grid[i][j]
                P1+=grid[i][j]*grid[i][j]
        print(S1,P1)
        print(S,P)
        s=S1-S
        diff=P1-P
        p=diff//s
        X=(s+p)//2
        Y=X-s
        return [X,Y]