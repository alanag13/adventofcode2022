input_file = __file__.split("/")
input_file[-1] = "input.txt"


def move_head(knot, nav):
    if nav == "R":
        knot[0] += 1

    elif nav == "L":
        knot[0] -= 1

    elif nav == "U":
        knot[1] += 1

    elif nav == "D":
        knot[1] -= 1


def move_tail(head, tail):
    x_dist, y_dist = head[0] - tail[0], head[1] - tail[1]
    max_dist = max(abs(x_dist), abs(y_dist))

    if max_dist >= 2:
        if x_dist > 0:
            tail[0] += 1
        elif x_dist < 0:
            tail[0] -= 1
        
        if y_dist > 0:
            tail[1] += 1
        elif y_dist < 0:
            tail[1] -= 1


with open("/".join(input_file)) as f:
    lines = f.readlines()


def get_unique_tail_positions(rope_len):
    visited = {(0, 0)}
    knots = [[0, 0] for _ in range(rope_len)]

    for line in lines:
        nav, dist = line.strip().split()

        for _ in range(int(dist)):
            move_head(knots[0], nav)

            for i in range(1, rope_len):
                move_tail(knots[i-1], knots[i])

            last_x, last_y = knots[-1]
            visited.add((last_x, last_y))

    return len(visited)

print(f"Part one: {get_unique_tail_positions(2)}")
print(f"Part two: {get_unique_tail_positions(10)}")
