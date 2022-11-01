class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        self.grid = grid
        self.row = len(grid)
        self.col = len(grid[0])
        res = []
        for i in range(self.col):
            res.append(self.isBallDrop(0,i))
            print("-----")
        return res
        
    def isBallDrop(self, m, n, top = 1, left = 0):
        print(m, n)
        if m >= self.row:
            return n
        if n >= self.col or n < 0:
            return -1
        if top:
            if self.grid[m][n] == 1:
                return self.isBallDrop(m, n+1, 0, 1)
            else:
                return self.isBallDrop(m, n-1, 0, 0)
            
        else:
            if left and self.grid[m][n] == -1:
                return -1
            elif left and self.grid[m][n] == 1:
                return self.isBallDrop(m+1, n, 1)
            elif left == 0 and self.grid[m][n] == -1:
                # print("--", m, n)
                return self.isBallDrop(m+1, n, 1, 0)
            elif left == 0 and self.grid[m][n] == 1:
                return -1
            else:
                print("new case: top left",top, left) 
                
            