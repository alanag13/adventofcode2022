input_file = __file__.split("/")
input_file[-1] = "input.txt"

def get_char_num(char):
    char_num = ord(char)

    if char_num >= 97:
        char_num -= 96
    
    else:
        char_num -= 38
    
    return char_num


with open("/".join(input_file)) as f:
    lines = f.readlines()

part_one_result = 0
part_two_result = 0
part_two_sets = [None, None, None]

for i in range(len(lines)):

    line = lines[i].strip()
    line_len = len(line)

    half = line_len // 2
    first = line[:half]
    last = line[half:]

    char = list(set(first).intersection(set(last)))[0]
    part_one_result += get_char_num(char)

    set_idx = i % 3
    part_two_sets[set_idx] = set(line)

    if set_idx == 2:
        char = list(part_two_sets[0].intersection(part_two_sets[1], part_two_sets[2]))[0]
        part_two_result += get_char_num(char)

print(f"Part one: {part_one_result}")
print(f"Part two: {part_two_result}")
