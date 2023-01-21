inp = [
  [5,3,0,0,7,0,0,0,0],
  [6,0,0,1,9,5,0,0,0],
  [0,9,8,0,0,0,0,6,0],
  [8,0,0,0,6,0,0,0,3],
  [4,0,0,8,0,3,0,0,1],
  [7,0,0,0,2,0,0,0,6],
  [0,6,0,0,0,0,2,8,0],
  [0,0,0,4,1,9,0,0,5],
  [0,0,0,0,8,0,0,7,9]
]


def getFreeFields(grid:list) -> list:
  freeFields = []

  for row in range(9):
    for col in range(9):
      if grid[row][col] == 0:
        freeFields.append((row, col))
    
  return freeFields


def validRow(grid:list, pos:tuple) -> bool:
  row, col = pos
  changed = grid[row][col]

  for i in range(9):
    if grid[row][i] == changed and i != col:
      return False

  return True


def validCol(grid:list, pos:tuple) -> bool:
  row, col = pos
  changed = grid[row][col]

  for i in range(9):
    if grid[i][col] == changed and i != row:
      return False

  return True


def validBlock(grid:list, pos:tuple) -> bool:
  row, col = pos
  changed = grid[row][col]

  rOff = (row // 3) * 3
  cOff = (col // 3) * 3

  for i in range(3):
    for j in range(3):
      if grid[rOff+i][cOff+j] == changed and (rOff+i, cOff+j) != pos:
        return False
  
  return True


def validCell(grid:list, pos:tuple) -> bool:
  x = validRow(grid, pos)
  y = validCol(grid, pos)
  z = validBlock(grid, pos)

  return x and y and z


def printGrid(grid:list) -> None:
  for i in grid:
    for j in i:
      print(j, end=" ")
    print()


def main(grid:list) -> list:
  freeFields = getFreeFields(grid)

  i = 0
  while i < len(freeFields):
    row, col = freeFields[i]

    if grid[row][col] == 9:
      grid[row][col] = 0
      i -= 1
      continue

    grid[row][col] += 1

    if validCell(grid, (row, col)):
      i += 1
  
  return grid


if __name__ == '__main__':
  out = main(inp)

  printGrid(out)