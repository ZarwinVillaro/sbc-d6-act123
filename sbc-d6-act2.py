r = int(input("Enter number of row: "))
columns = int(input("Enter number of column: "))

rows = 0
while rows < r:
  col = 0

  while col < columns:
    if rows == 0 or rows == r - 1 or col == 0 or col == columns - 1:
      print("*", end="")
      
    else:
      print(" ", end="")
    col += 1
  print("")
  rows += 1