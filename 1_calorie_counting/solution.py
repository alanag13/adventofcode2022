input_file = __file__.split("/")
input_file[-1] = "input.txt"

from heapq import heappop, heappush

curr_sum = 0
max_sum = 0
max_heap = []

with open("/".join(input_file)) as f:
    lines = f.readlines()

for i in range(len(lines)):
    num = lines[i].strip()

    if not num or i == len(lines) - 1:
        heappush(max_heap, curr_sum)

        if len(max_heap) > 3:
            heappop(max_heap)

        max_sum = max(max_sum, curr_sum)
        curr_sum = 0
        
        continue

    curr_sum += int(num)

print(f"Part one: {max_sum}")
print(f"Part two: {sum(max_heap)}")
