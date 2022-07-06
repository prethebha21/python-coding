m1 = [list(map(int, input("Enter row: ").split(" ")))
      for i in range(int(input("Enter Number of rows: ")))]
m2 = [list(map(int, input("Enter row: ").split(" ")))
      for i in range(int(input("Enter Number of rows:")))]
print("Add Matrix:")
r = [[m1[i][j] + m2[i][j]
      for j in range(len(m1[0]))] for i in range(len(m1))]
print(r)
print("Subtract Matrix:")
r = [[m1[i][j] - m2[i][j]
      for j in range(len(m1[0]))] for i in range(len(m1))]
print(r)