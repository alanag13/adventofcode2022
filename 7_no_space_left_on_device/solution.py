from math import inf

input_file = __file__.split("/")
input_file[-1] = "input.txt"

class Node:
    def __init__(self):
        self._children = []
        self._size = 0
        self._calculated = False
        self._total = 0

    def add_child(self, node):
        self._children.append(node)

    def incr_size(self, size):
        self._size += size

    def get_size(self):
        if not self._calculated:
            self._total = self._size + sum(child.get_size() for child in self._children)

        return self._total


with open("/".join(input_file)) as f:
    lines = f.readlines()

directory_hist = ["/"]
directories = {"/": Node()}


def get_cur_dir():
    return "/".join(directory_hist)


def add_dir(dir_name):
    curr_dir = get_cur_dir()
    directory = curr_dir + "/" + dir_name

    if directory not in directories:
        node = Node()
        directories[directory] = node
        directories[curr_dir].add_child(node)

def cd(directory):
    add_dir(directory)
    
    if directory == "/":
        directory_hist.clear()
        directory_hist.append("/")
        return

    if directory == "..":
        directory_hist.pop()
        return

    directory_hist.append(directory)


def process(line):
    parts = line.split()
    if parts[0] == "$":
        if parts[1] == "cd":
            cd(parts[2])

    elif parts[0] != "dir":
        directories[get_cur_dir()].incr_size(int(parts[0]))
 

for i in range(len(lines)):
    line = lines[i].strip()
    process(line)

total_size = 0
min_dir_to_delete = inf

free_space = 70000000 - directories["/"].get_size()
required_additional_free_space = 30000000 - free_space

for node in directories.values():
    size = node.get_size()
    if size <= 100000:
        total_size += size
    if size >= required_additional_free_space:
        min_dir_to_delete = min(min_dir_to_delete, size)

print(f"Part one: {total_size}")
print(f"Part two: {min_dir_to_delete}")