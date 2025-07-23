# 36 v1 - valid sudoku

def validSudoku(board):
  rws = [set() for _ in range(9)]
  cls = [set() for _ in range(9)]
  bxs = [set() for _ in range(9)]

  for r in range(9):
    for c in range(9):
      val = board[r][c]
      if val =='.':
        continue 

      if (val in rws[r] or 
          val in cls[c] or 
          val in bxs[(r // 3) * 3 + (c // 3)]):
        return False

      rws[r].add(val)
      cls[c].add(val)
      bxs[(r // 3) * 3 + (c // 3)].add(val)

  return True