lines = open("/home/aurelien/AOC/2023/aoc5.txt").read().splitlines()

seeds = [int(x) for x in lines[0].split(":")[1].strip().split(" ")]
print(seeds)

almanac = []
map = []
for line in lines[2:]:
    if line != "":
        if line.endswith("map:"):
            if map != []:
                almanac.append(map)
            map = []
        else:
            map.append([int(x) for x in line.split(" ")])
almanac.append(map)


def first_star(seeds, almanac):
    for a in almanac:
        for i, s in enumerate(seeds):
            for end, start, r in a:
                if s in range(start, start + r):
                    seeds[i] = end + (s - start)
                    break
    return min(seeds)


def second_star(seeds, almanac):
    starts = seeds[::2]
    ranges = seeds[1::2]
    res = float("inf")
    for s, r in zip(starts, ranges):
        for x in range(s, s + r):
            location = first_star([x], almanac)
            res = res if res < location else location
    return res


print(first_star(seeds, almanac))

seeds = [int(x) for x in lines[0].split(":")[1].strip().split(" ")]

print(second_star(seeds, almanac))
