class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def is_valid(r, c, ch):
            # check row
            for i in range(9):
                if board[r][i] == ch:
                    return False
            
            # check column
            for i in range(9):
                if board[i][c] == ch:
                    return False
            
            # check 3×3 subgrid
            start_row = (r // 3) * 3
            start_col = (c // 3) * 3
            
            for i in range(3):
                for j in range(3):
                    if board[start_row + i][start_col + j] == ch:
                        return False
            
            return True
        
        def solve():
            for r in range(9):
                for c in range(9):
                    if board[r][c] == ".":
                        for ch in "123456789":
                            if is_valid(r, c, ch):
                                board[r][c] = ch
                                if solve():  
                                    return True
                                board[r][c] = "."   # backtrack
                        return False
            return True  # solved
        
        solve()