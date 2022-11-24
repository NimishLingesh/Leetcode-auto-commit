class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        direction = [[0,1], [1,0], [0,-1], [-1, 0]]
        visited = set()
        rows = len(board)
        cols = len(board[0])
        def helper(r, c, word):
            if len(word) == 0:
                return True
            for point in direction:
                if r+point[0] >= 0 and c+point[1] >=0 and r+point[0] < rows and c+point[1] < cols and board[r+point[0]][c+point[1]] == word[0] and (r+point[0], c+point[1]) not in visited:
                    visited.add((r+point[0], c+point[1]))
                    # print(r+point[0], c+point[1])
                    if len(word) == 1:
                        return True
                    resp = helper(r+point[0], c+point[1], word[1:])
                    if resp:
                        return True
                    else:
                        visited.remove((r+point[0], c+point[1]))
            return False
            
        for r_idx, row in enumerate(board):
            for c_idx, col in enumerate(row):
                if board[r_idx][c_idx] == word[0]:
                    visited = set()
                    visited.add((r_idx, c_idx))
                    res = helper(r_idx, c_idx, word[1:])
                    if res:
                        return True
        return False