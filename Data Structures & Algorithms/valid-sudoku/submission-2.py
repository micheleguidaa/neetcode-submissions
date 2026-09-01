from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict_row = defaultdict(set)
        dict_column = defaultdict(set)
        dict_section = defaultdict(set)

        for i in range(9):
            for j in range(9):
                if (board[i][j] in dict_row[i] 
                or board[i][j] in dict_column[j]
                or board[i][j] in dict_section[(i//3, j//3)]):
                    return False
                if board[i][j] == ".":
                    continue
                dict_row[i].add(board[i][j])
                dict_column[j].add(board[i][j])
                dict_section[(i//3,j//3)].add(board[i][j])
        return True

        