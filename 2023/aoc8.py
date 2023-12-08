import math

lines = open("/home/aurelien/AOC/2023/aoc8.txt").read().splitlines()

instruction = lines[0]
tree = {}
for line in lines[2:]:
    key = line.split(" =")[0]
    left = line.split(" (")[1].split(", ")[0]
    right = line.split(", ")[1].split(")")[0]
    tree[key] = {"L": left, "R": right}


def first_star(instruction, tree):
    count = 0
    node = "AAA"
    while node != "ZZZ":
        node = tree[node][instruction[(count) % len(instruction)]]
        count += 1
    return count


def count_steps(start, instruction, tree):
    node = start
    count = 0
    while not node.endswith("Z"):
        node = tree[node][instruction[(count) % len(instruction)]]
        count += 1
    return count


def second_star(instruction, tree):
    nodes = [n for n in tree if n.endswith("A")]
    return math.lcm(*[count_steps(n, instruction, tree) for n in nodes])


print(first_star(instruction, tree))
print(second_star(instruction, tree))
