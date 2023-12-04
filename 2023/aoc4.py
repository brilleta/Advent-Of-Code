lines = open("/home/aurelien/AOC/2023/aoc4.txt").read().splitlines()


def first_star(lines):
    count = 0
    for line in lines:
        line = line.split(":")[1]
        parts = [x.split(" ") for x in line.split("|")]
        win = set(int(x) for x in filter(lambda a: a != "", parts[0]))
        number = set(int(x) for x in filter(lambda a: a != "", parts[1]))
        size = len(win.intersection(number))
        count += 0 if size == 0 else 2 ** (size - 1)
    return count


def second_star(lines):
    cards = [1 for _ in range(len(lines))]
    for i, line in enumerate(lines):
        line = line.split(":")[1]
        parts = [x.split(" ") for x in line.split("|")]
        win = set(int(x) for x in filter(lambda a: a != "", parts[0]))
        number = set(int(x) for x in filter(lambda a: a != "", parts[1]))
        size = len(win.intersection(number))
        if size > 0:
            for j in range(size):
                cards[i + j + 1] += cards[i]
    return sum(cards)


print(first_star(lines))
print(second_star(lines))
