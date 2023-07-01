''' 
Problem Statement: https://leetcode.com/problems/validate-sudoku/

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated according to the mentioned rules.
'''

'''
Initial Thoughts:

- Validate each of the 9 rows (O(1))
- Validate each of the 9 cols (O(1))
- Validate each of the 9 subgrids (O(1))

Approach:
- Use hashing to ensure no duplicate member in row / col / subgrid
- Clear hashset after each row / col / subgrid
- O(1) time complexity, O(1) space complexity
'''

NUM_ROWS = 9
NUM_COLS = 9
NUM_GRID_ROWS = 3
NUM_GRID_COLS = 3

def check_row_constraints(board):
    row_set = set()
    
    for r in range(NUM_ROWS):
        for c in range(NUM_COLS):
            curr_digit = board[r][c]
            if curr_digit in row_set:
                return False
            if curr_digit != ".":
                row_set.add(board[r][c])
        row_set.clear()

    return True

def check_col_constraints(board):
    col_set = set()
    for c in range(NUM_COLS):
        for r in range(NUM_ROWS):
            curr_digit = board[r][c]
            if curr_digit in col_set:
                return False
            if curr_digit != ".":
                col_set.add(board[r][c])
        col_set.clear()

    return True

def check_subgrid_constraints(board):
    grid_set = set()

    for grid_row in range(NUM_GRID_ROWS):
        for grid_col in range(NUM_GRID_COLS):
            for r in range(NUM_ROWS / NUM_GRID_ROWS):
                for c in range(NUM_COLS / NUM_GRID_COLS):
                    curr_digit = board[grid_row * 3 + r][grid_col * 3 + c]
                    if curr_digit in grid_set:
                        return False
                    if curr_digit != ".":
                        grid_set.add(board[grid_row * 3 + r][grid_col * 3 + c])

            grid_set.clear()
    
    return True

def is_valid_sudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    return check_row_constraints(board) and check_col_constraints(board) and check_subgrid_constraints(board)