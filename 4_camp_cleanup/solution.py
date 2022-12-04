input_file = __file__.split("/")
input_file[-1] = "input.txt"

with open("/".join(input_file)) as f:
    lines = f.readlines()

def get_range(str):
    _min, _max = str.split('-')
    return int(_min), int(_max)

def get_ranges(line):
    first, second = line.split(',')
    return get_range(first), get_range(second)

def range_contains_other(first, second):
    first_min, first_max = first
    second_min, second_max = second

    return (first_min <= second_min and second_max <= first_max) or \
        (second_min <= first_min and first_max <= second_max)

def range_overlaps_other(first, second):
    first_min, first_max = first
    second_min, second_max = second

    return not (first_max < second_min or second_max < first_min)
 
part_one_count = 0
part_two_count = 0

for i in range(len(lines)):
    line = lines[i].strip()
    first_range, second_range = get_ranges(line)

    if range_contains_other(first_range, second_range):
        part_one_count += 1
        part_two_count += 1

    elif range_overlaps_other(first_range, second_range):
        part_two_count += 1

print(f"Part one: {part_one_count}")
print(f"Part two: {part_two_count}")
