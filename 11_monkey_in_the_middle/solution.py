from collections import deque

input_file = __file__.split("/")
input_file[-1] = "input.txt"

with open("/".join(input_file)) as f:
    chunks = f.read().split("\n\n")


class Monkey:

    def __init__(self, items, op, test_divisor, t_target, f_target):
        self._items = items
        self._op = op
        self._inspected = 0
        self.t_target = t_target
        self.f_target = f_target
        self.test_divisor = test_divisor

    def _next_item(self, item):
        left, op, right = self._op
        if left == "old":
            left = item

        if right == "old":
            right = item

        if op == "*":
            return int(left) * int(right)
        else:
            return int(left) + int(right)
    
    def get_num_inspected(self):
        return self._inspected

    def receive(self, item):
        self._items.append(item)

    def next_item(self):
        if self._items:
            self._inspected += 1

            item = self._items.popleft()
            item = self._next_item(item)
            return item
        
        return None
        

class MonkeyWorld:
    def __init__(self, monkey_list, reducer):
        self._monkey_list = monkey_list
        self._reducer = reducer

    def _do_turn(self, monkey, next_item):
        while next_item is not None:
            if next_item:
                to_throw = self._reducer(next_item)
                if to_throw % monkey.test_divisor == 0:
                    self._monkey_list[monkey.t_target].receive(to_throw)
                else:
                    self._monkey_list[monkey.f_target].receive(to_throw)
            next_item = monkey.next_item()

    def do_round(self):
        for monkey in self._monkey_list:
            next_item = monkey.next_item()
            self._do_turn(monkey, next_item)

    def get_monkey_business(self):
        most_inspected = sorted(
            self._monkey_list,
            key=lambda x: x.get_num_inspected(),
            reverse=True
        )
        return most_inspected[0].get_num_inspected() * most_inspected[1].get_num_inspected()


def parse_chunk(chunk):
    lines = chunk.split("\n")
    items = deque(int(item) for item in lines[1].split(": ")[1].split(", "))
    op = lines[2].split(" = ")[1].strip().split()
    test_divisor = int(lines[3].split('by')[1])
    t_target = int(lines[4].split("monkey")[1])
    f_target = int(lines[5].split("monkey")[1])
    return Monkey(items, op, test_divisor, t_target, f_target)


def build_monkey_list():
    monkey_list = []
    mod = 1

    for chunk in chunks:
        monkey = parse_chunk(chunk)
        monkey_list.append(monkey)
        mod *= monkey.test_divisor

    return monkey_list, mod

list_two, mod = build_monkey_list()
list_one, _ = build_monkey_list()

part_one = MonkeyWorld(list_one, lambda x: x // 3)
part_two = MonkeyWorld(list_two, lambda x: x % mod)

for _ in range(20):
    part_one.do_round()

for _ in range(10000):
    part_two.do_round()

print(f"Part one: {part_one.get_monkey_business()}")
print(f"Part two: {part_two.get_monkey_business()}")
    
    