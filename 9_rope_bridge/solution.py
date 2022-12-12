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

        # print(visited)
        # print(prev_head)
        # print(head)
        # print() 
    #     prev_head_x, prev_head_y = head
    #     move(head, nav)
    #     print(head)
    #     print()
    #     x, y = head

    #     if x == prev_head_x or y == prev_head_y:
    #         visited.append((prev_head_x, prev_head_y))

    #     if max_dist >= 2:
    #         prev_head_x, prev_head_y = x, y
        

        # if (tail[0] == head[0] and abs(tail[1] - head[1]) >= 2) or \
        # (tail[1] == head[1] and abs(tail[0] - head[0]) >= 2):

        #     move(tail, nav)

        # elif (tail[0] != head[0] and tail[1] != head[1]):
        #     x_dist, y_dist = abs(tail[0] - head[0]), abs(tail[1] - head[1])
        #     max_dist = max(x_dist, y_dist)

        #     if max_dist >= 2:
        #         tail = [prev_head_x, prev_head_y]

        # head = tail

print(len(set(visited)))