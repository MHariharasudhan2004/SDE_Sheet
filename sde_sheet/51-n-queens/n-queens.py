class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        posDiag=set()
        NegDiag=set()
        board=[['.']*n for i in range(n)]
        res=[]
        def backtrack(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return 
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in NegDiag:
                    continue
                col.add(c)
                posDiag.add(r+c)
                NegDiag.add(r-c)
                board[r][c]="Q"
                backtrack(r+1)
                col.remove(c)
                posDiag.remove(r+c)
                NegDiag.remove(r-c)
                board[r][c]="."
        backtrack(0)
        return res
        