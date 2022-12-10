from math import inf

input_file = __file__.split("/")
input_file[-1] = "input.txt"


with open("/".join(input_file)) as f:
    lines = f.readlines()

width = len(lines[0].strip())
height = len(lines)

grid = [[int(num) for num in list(line.strip())] for line in lines]

viz_grid = [[0] * width for _ in range(height)]
scenic_grid = [[0] * width for _ in range(height)]


def populate_cells(max_seen, row, col):
    val = grid[row][col]

    if max_seen < val:
        max_seen = val
        viz_grid[row][col] = True

    return max_seen


def populate_grid(grid):
    height = len(grid)
    width =  len(grid[0])

    for i in range(height):
        max_l, max_r = -inf, -inf
        l_idx, r_idx = 0, width - 1

        while l_idx <= width - 1 and r_idx >= 0:
            max_l = populate_cells(max_l, i, l_idx)
            max_r = populate_cells(max_r, i, r_idx)

            l_idx += 1
            r_idx -= 1

    for k in range(width):
        max_u, max_b = -inf, -inf
        u_idx, b_idx = 0, height - 1

        while u_idx <= height - 1 and b_idx >= 0:
            max_u = populate_cells(max_u, u_idx, k)
            max_b = populate_cells(max_b, b_idx, k)

            u_idx += 1
            b_idx -= 1


populate_grid(grid)

count = 0

for row in viz_grid:
    for cell in row:
        if cell:
            count += 1

print(count)
# print(scenic_grid)





