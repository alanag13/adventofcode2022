input_file = __file__.split("/")
input_file[-1] = "input.txt"

with open("/".join(input_file)) as f:
    lines = f.readlines()


class CathodeRayTube:
    def __init__(self, next_check, last_check):
        self._next_check = next_check
        self._last_check = last_check
        self._X = 1
        self._result = 0
        self._cycle = 0
        self._output = []

    def tick_cycle(self):
        pixel_pos = (self._cycle % 40)
        self._cycle += 1

        if abs(pixel_pos - self._X) <= 1:
            self._output.append("#")
        else:
            self._output.append(".")

        if self._cycle >= self._next_check and self._cycle <= self._last_check:
            self._output.append("\n")
            self._result += (self._X * self._cycle)
            self._next_check += 40

    def incr_x(self, amount):
        self._X += amount

    def get_signal_strength(self):
        return self._result

    def get_pixel_output(self):
        return "".join(self._output)

part_one = CathodeRayTube(20, 220)
part_two = CathodeRayTube(40, 240)

for line in lines:
    part_one.tick_cycle()
    part_two.tick_cycle()
    parts = line.strip().split()
    cmd = parts[0]

    if cmd != "noop":
        part_one.tick_cycle()
        part_two.tick_cycle()
        part_one.incr_x(int(parts[1]))
        part_two.incr_x(int(parts[1]))

print(f"Part one: {part_one.get_signal_strength()}\n")
print("Part two:")
print(part_two.get_pixel_output())