class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=time=0
        q=deque()
        rows=len(grid)
        cols=len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    q.append([i,j])
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        while fresh>0 and q:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in directions:
                    row,col=dr+r,dc+c
                    if (row<0 or row==len(grid) or
                        col<0 or col==len(grid[0]) or
                        grid[row][col]!=1):
                        continue
                    grid[row][col]=2
                    q.append([row,col])
                    fresh-=1
            time+=1
        return time if fresh==0 else -1


        