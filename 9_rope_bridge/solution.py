input_file = __file__.split("/")
input_file[-1] = "input.txt"

visited = [(0, 0)]

head, prev_head = (0, 0), (0, 0)

def move(knot, nav):
    x, y = knot

    if nav == "R":
        x += 1

    elif nav == "L":
        x -= 1

    elif nav == "U":
        y += 1

    elif nav == "D":
        y -= 1

    return x, y


with open("/".join(input_file)) as f:
    lines = f.readlines()

knots = [(0, 0)]

for line in lines:
    nav, dist = line.strip().split()

    for idx in range(int(dist)):
        orig_head = head
        head = move(head, nav)
        x, y = head
        prev_x, prev_y = prev_head

        x_dist, y_dist = abs(prev_x - x), abs(prev_y - y)
        total_dist = max(x_dist, y_dist)

        if total_dist >= 2:
            prev_head = orig_head
            visited.append(prev_head)

print(len(set(visited)))