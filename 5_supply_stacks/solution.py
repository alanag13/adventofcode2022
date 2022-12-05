from collections import deque

input_file = __file__.split("/")
input_file[-1] = "input.txt"

with open("/".join(input_file)) as f:
    boxes, moves = f.read().split("\n\n")
    box_lines = boxes.splitlines()
    move_lines = moves.splitlines()

line_len = len(box_lines[0])
columns = (line_len + 1) // 4

part_one_stacks = [deque() for _ in range(columns)]
part_two_stacks = [deque() for _ in range(columns)]

def add_line_to_stacks(line):
    for column in range(columns):
        start = column * 4
        end = min(line_len, start + 3)
        box = line[start:end][1].strip()
        if box:
            part_one_stacks[column].append(box)
            part_two_stacks[column].append(box)

def parse_moves(line):
    halves = line.split(' from ')
    move, from_to = halves[0], halves[1]
    quantity = move.split()[1]
    directions = from_to.split(' to ')
    source, dest = directions[0], directions[1]
    return int(quantity), int(source), int(dest)


for line in box_lines:
    if line.strip()[0] != '1':
        add_line_to_stacks(line)

for line in move_lines:
    quantity, source, dest = parse_moves(line)

    from_idx, to_idx = source - 1, dest - 1
    part_two_boxes = deque()

    for _ in range(int(quantity)):
        part_one_box = part_one_stacks[from_idx].popleft()
        part_one_stacks[to_idx].appendleft(part_one_box)

        part_two_box = part_two_stacks[from_idx].popleft()
        part_two_boxes.appendleft(part_two_box)

    part_two_stacks[to_idx].extendleft(part_two_boxes)

part_one_result = "".join(stack.popleft() for stack in part_one_stacks)
part_two_result = "".join(stack.popleft() for stack in part_two_stacks)

print(f"Part one: {part_one_result}")
print(f"Part two: {part_two_result}")