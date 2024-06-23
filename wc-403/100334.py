# Find the Minimum Area to Cover All Ones I

grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [1, 0, 1]]

row_size = []
col_size = []

m = len(grid[0])
n = len(grid)

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            row_size.append(i)
            col_size.append(j)
row_size = list(set(row_size))
col_size = list(set(col_size))

row_size.sort()
col_size.sort()

min_row = min(row_size)
max_row = max(row_size)

min_col = min(col_size)
max_col = max(col_size)

area = (max_row-min_row+1)*(max_col-min_col+1)
print(area)
