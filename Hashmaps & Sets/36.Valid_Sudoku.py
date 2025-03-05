class Solution:
    # O(N^2)
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        # Rows
        for row in board:
            seen.clear()
            for cell in row:
                if cell.isnumeric():
                    if cell not in seen:
                        seen.add(cell)
                    else:
                        return False
        
        # Cols
        for j in range(9):
            seen.clear()
            for i in range(9):
                cell = board[i][j]
                if cell.isnumeric():
                    if cell not in seen:
                        seen.add(cell)
                    else:
                        return False
        
        # Boxes
        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                seen.clear()
                i = row
                for i in range(i, i + 3):
                    j = col
                    for j in range(j, j + 3):
                        cell = board[i][j]
                        if cell.isnumeric():
                            if cell not in seen:
                                seen.add(cell)
                            else:
                                return False

        return True
    
    # O(N^2)
    # Another solution I find beutiful although it is not mine
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i, row in enumerate(board):
            for j, x in enumerate(row):
                if x != '.':
                    res += [(i, x), (x, j), (i // 3, j // 3, x)]
        return len(res) == len(set(res))