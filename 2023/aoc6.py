lines = open("/home/aurelien/AOC/2023/aoc6.txt").read().splitlines()

lines = [x.split(":")[1].strip().split(" ") for x in lines]
time = [int(x) for x in filter(lambda a: a != "", lines[0])]
distance = [int(x) for x in filter(lambda a: a != "", lines[1])]


def get_wins(overall_time, distance_to_beat):
    count = 0
    for press_time in range(overall_time):
        if (overall_time - press_time) * press_time > distance_to_beat:
            count += 1
    return count


def first_star(t, d):
    res = 1
    for overall_time, distance_to_beat in zip(t, d):
        res *= get_wins(overall_time, distance_to_beat)
    return res


def second_star(t, d):
    return get_wins(t, d)


print(first_star(time, distance))

time = int("".join(str(x) for x in time))
distance = int("".join(str(x) for x in distance))

print(second_star(time, distance))
