input_file = __file__.split("/")
input_file[-1] = "input.txt"

def get_result(theirs, mine):
    if mine == theirs:
        return 3

    if (1 + (theirs % 3)) == mine:
        return 6

    return 0

with open("/".join(input_file)) as f:
    records = f.readlines()
    
part_one_score = 0
part_two_score = 0

for i in range(len(records)):
    theirs, mine = records[i].split()
    their_shape = (ord(theirs) - 65) + 1
    part_one_my_shape = (ord(mine) - 23) - 65 + 1
    part_two_my_shape = ((their_shape + part_one_my_shape) % 3) + 1
    part_one_score += (
        part_one_my_shape + get_result(their_shape, part_one_my_shape)
    )
    part_two_score += (
        part_two_my_shape + get_result(their_shape, part_two_my_shape)
    )

print(f"Part one: {part_one_score}")
print(f"Part two: {part_two_score}")
