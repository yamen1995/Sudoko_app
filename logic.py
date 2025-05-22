import random
def is_sudoku_solved(board):
    for i in range(9):
        row = set()
        col = set()
        box = set()
        for j in range(9):
            # Check for empty cell
            if board[i][j] == '.' or board[j][i] == '.':
                return False

            # Check row
            if board[i][j] in row:
                return False
            row.add(board[i][j])

            # Check column
            if board[j][i] in col:
                return False
            col.add(board[j][i])

            # Check 3x3 box
            box_row = 3 * (i // 3)
            box_col = 3 * (i % 3)
            row_offset = j // 3
            col_offset = j % 3
            val = board[box_row + row_offset][box_col + col_offset]
            if val == '.' or val in box:
                return False
            box.add(val)

    return True
def check_board(board):
    if is_sudoku_solved(board):
        return True
    else:
        return False
def solve_sudoku(board):
  nums=["1","2","3","4","5","6","7","8","9"]
  for r in range(9):
    for c in range(9):
      if board[r][c] in ". ":
         for i in nums:
          board[r][c]=i
          if is_valid_sudoku(board):
            if solve_sudoku(board)[0]:return [True, board]
          board[r][c]="."
         return [False,board]
  return [True, board]
       
def is_valid_sudoku(board):
    for i in range(9):
        row = set()
        col = set()
        box = set()
        for j in range(9):
            # Check row
            if board[i][j] not in '. ':
                if board[i][j] in row:
                    return False
                row.add(board[i][j])
            # Check column
            if board[j][i] not in '. ':
                if board[j][i] in col:
                    return False
                col.add(board[j][i])
            # Check 3x3 box
            box_row = 3 * (i // 3) + j // 3
            box_col = 3 * (i % 3) + j % 3
            val = board[box_row][box_col]
            if val not in '. ':
                if val in box:
                    return False
                box.add(val)
    return True

def generate_full_board():
    board = [["." for _ in range(9)] for _ in range(9)]
    fill_board(board)
    return board

def fill_board(board):
    nums = list("123456789")
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                random.shuffle(nums)
                for num in nums:
                    board[r][c] = num
                    if is_valid_sudoku(board) and fill_board(board):
                        return True
                    board[r][c] = "."
                return False
    return True

def generate_puzzle_board(empty_cells=40):
    board = generate_full_board()
    attempts = 0
    while attempts < empty_cells:
        r = random.randint(0, 8)
        c = random.randint(0, 8)
        if board[r][c] != ".":
            board[r][c] = "."
            attempts += 1
    return board
