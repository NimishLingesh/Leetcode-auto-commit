class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        
        for r in range(row-1):
            for c in range(col-1):
                if matrix[r][c] != matrix[r+1][c+1]:
                    return False
        return True