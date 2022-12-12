from math import inf

input_file = __file__.split("/")
input_file[-1] = "input.txt"


with open("/".join(input_file)) as f:
    lines = f.readlines()

width = len(lines[0].strip())
height = len(lines)

grid = [[int(num) for num in list(line.strip())] for line in lines]

viz_grid = [[False] * width for _ in range(height)]
scenic_grid = [[1] * width for _ in range(height)]


def populate_grids():

    for i in range(height):
        populate_row(i)

    for k in range(width):
        populate_col(k)


def populate_row(row_idx):
    max_l, max_r = -inf, -inf
    l, r = 0, width - 1
    l_walls, r_walls = [], []

    while l <= width - 1 and r >= 0:

        max_l = populate_viz_cell(max_l, row_idx, l)
        max_r = populate_viz_cell(max_r, row_idx, r)

        l_walls = set_scenic_cell(l_walls, (row_idx, l), 1)
        r_walls = set_scenic_cell(r_walls, (row_idx, r), 1)

        l += 1
        r -= 1


def populate_col(col_idx):
    max_u, max_d = -inf, -inf
    u, d = 0, height - 1
    u_walls, d_walls = [], []

    while u <= height - 1 and d >= 0:
        max_u = populate_viz_cell(max_u, u, col_idx)
        max_d = populate_viz_cell(max_d, d, col_idx)

        u_walls = set_scenic_cell(u_walls, (u, col_idx), 0)
        d_walls = set_scenic_cell(d_walls, (d, col_idx), 0)

        u += 1
        d -= 1


def populate_viz_cell(max_seen_val, row, col):
    val = grid[row][col]

    if max_seen_val < val:
        max_seen_val = val
        viz_grid[row][col] = True

    return max_seen_val


def set_scenic_cell(walls, coords, check):
    
    def get_nearest_wall():
        wall = walls[-1]
        wall_row, wall_col = wall
        wall_val = grid[wall_row][wall_col]
        wall_idx = wall[check]
        return wall_val, wall_idx

    def get_dist_from_origin(curr_idx, wall_idx):
        if curr_idx > wall_idx:
            dist = wall_idx
        else:
            dist = width - wall_idx - 1 if check == 0 else height - wall_idx - 1
        return dist

    row, col = coords
    val = grid[row][col]

    if not walls:
        scenic_grid[row][col] = 0
        walls = [(row, col)]
    else:
        curr_idx = coords[check]
        wall_val, wall_idx = get_nearest_wall()
        visible = 1

        while wall_val < val and walls:
            walls.pop()
            if walls:
                wall_val, wall_idx = get_nearest_wall()

        visible = abs(curr_idx - wall_idx)

        if not walls and wall_val < val:
            visible += get_dist_from_origin(curr_idx, wall_idx)

        scenic_grid[row][col] *= visible
        
        walls.append((row, col))

    return walls
    

populate_grids()

viz_count = 0

for row in viz_grid:
    for cell in row:
        if cell:
            viz_count += 1

print(viz_count)
print(max((max((col for col in rows)) for rows in scenic_grid)))
