from math import inf
from heapq import heappop, heappush

input_file = __file__.split("/")
input_file[-1] = "input.txt"

with open("/".join(input_file)) as f:
    lines = f.readlines()


def get_height(char):
    if char == "S":
        return 1

    if char == "E":
        return 26

    return ord(char) - 96

class MinStepsSolver:
    def __init__(self, lines, start_char, compare_height):
        self._compare_height = compare_height
        self._height = len(lines)
        self._width = len(lines[0].strip())
        self._grid = []
        self._distances = {}
        self._min_heap = []
        self._initialize(lines, start_char)

    def _initialize(self, lines, start_char):
        for i in range(self._height):
            self._grid.append([])
            chars = list(lines[i].strip())
            for k in range(len(chars)):
                self._grid[i].append(chars[k])
                if chars[k] == start_char:
                    self._distances[(i, k)] = 0
                    self._min_heap = [(0, (i , k))]

    def _get_reachable_neighbors(self, row, col):
        neighbors = []
        curr_height = get_height(self._grid[row][col])

        for y, x in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if row + y < 0 or col + x < 0 or \
               row + y >= self._height or col + x >= self._width:
                continue

            neighbor_height = get_height(self._grid[row + y][col + x])
            if self._compare_height(neighbor_height, curr_height):
                neighbors.append((row + y, col + x))

        return neighbors

    def get_min_dist_to_end_char(self, end_char):
        min_dist = inf

        while self._min_heap:
            curr_y, curr_x = heappop(self._min_heap)[1]
            if self._grid[curr_y][curr_x] == end_char:
                min_dist = min(min_dist, self._distances[(curr_y, curr_x)])

            for y, x in self._get_reachable_neighbors(curr_y, curr_x):
                dist = self._distances[(curr_y, curr_x)] + 1
                if (y, x) not in self._distances:
                    heappush(self._min_heap, (dist, (y, x)))
                    self._distances[(y, x)] = dist
                else:
                    self._distances[(y, x)] = min(self._distances[(y, x)], dist)

        return min_dist

part_one = MinStepsSolver(lines, "S", lambda n, c: n <= c + 1)
part_two = MinStepsSolver(lines, "E", lambda n, c: n >= c - 1)

print(f"Part one: {part_one.get_min_dist_to_end_char('E')}")
print(f"Part two: {part_two.get_min_dist_to_end_char('a')}")
