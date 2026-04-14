class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row = set()
            for j in range(len(board[i])):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])
        
        for i in range(len(board)):
            column = set()
            for j in range(len(board)):
                if board[j][i] != ".":
                    if board[j][i] in column:
                        return False
                    column.add(board[j][i])
        
        for i in range(3):
            for j in range(3):
                box = set()
                for r in range(3):
                    for c in range(3):
                        if board[r+(3*i)][c+(3*j)] !=".":
                            if board[r+(3*i)][c+(3*j)] in box:
                                return False
                            box.add(board[r+(3*i)][c+(3*j)])
        return True
            