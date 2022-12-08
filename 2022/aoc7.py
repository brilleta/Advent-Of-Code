from itertools import chain

lines = open("/home/aurelien/AOC/2022/aoc7.txt").read().splitlines()


file_system = {"/": {}}
path = []


def get_element(fs, path):
    for p in path:
        fs = fs[p]
    return fs


def get_size(dict, element):
    if type(dict[element]) == int:
        return dict[element]
    return sum([get_size(dict[element], e) for e in dict[element]])


def get_list_size(res, dict, element):
    if type(dict[element]) == int:
        return []
    return (
        res
        + [get_size(dict, element)]
        + [get_list_size(res, dict[element], x) for x in dict[element]]
    )


def flatten(l):
    try:
        return (
            flatten(l[0]) + (flatten(l[1:]) if len(l) > 1 else [])
            if type(l) is list
            else [l]
        )
    except IndexError:
        return []


for i, line in enumerate(lines):
    split = line.split(" ")
    first_word = split[0]
    if first_word == "$":
        command = split[1]
        if command == "cd":
            if split[2] == "..":
                path.pop()
            else:
                path.append(split[2])
        elif command == "ls":
            current = get_element(file_system, path)
            j = 1
            while i + j < len(lines) and lines[i + j].split(" ")[0] != "$":
                split = lines[i + j].split(" ")
                if split[0] == "dir":
                    current[split[1]] = {}
                else:
                    current[split[1]] = int(split[0])
                j += 1
size_fs = get_size(file_system, "/")
l_size = get_list_size([], file_system, "/")
print(l_size)
flatten_size = flatten(l_size)
remaining_space = 70_000_000 - size_fs

print(sum(x for x in flatten_size if x <= 100000))
print(size_fs)
print(sorted(x for x in flatten_size))
print(min(x for x in flatten_size if (30_000_000 - remaining_space) <= x))
