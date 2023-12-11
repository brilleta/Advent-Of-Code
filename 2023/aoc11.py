import itertools
import math
import typing as t

lines = open("/home/aurelien/AOC/2023/aoc11.txt").read().splitlines()

universe = [list(line) for line in lines]


def expand(universe: t.List[t.List[str]]) -> t.List[t.List[str]]:
    univ = []
    for row in universe:
        if set(row) == {"."}:
            univ.append(row)
        univ.append(row)
    res = []
    for i in range(len(univ)):
        temp = []
        for j in range(len(univ[i])):
            if all(univ[k][j] == "." for k in range(len(univ))):
                temp.append(univ[i][j])
            temp.append(univ[i][j])
        res.append(temp)
    return res


def expand2(universe: t.List[t.List[str]]) -> t.List[t.List[str]]:
    univ = []
    for row in universe:
        if set(row) == {"."}:
            univ.append(["E" for _ in range(len(row))])
        univ.append(row)
    res = []
    for i in range(len(univ)):
        temp = []
        for j in range(len(univ[i])):
            if all(univ[k][j] != "#" for k in range(len(univ))):
                temp.append("E")
            temp.append(univ[i][j])
        res.append(temp)
    return res


def get_coords(universe: t.List[t.List[str]]) -> t.List[t.Tuple[int, int]]:
    coords = []
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == "#":
                coords.append((i, j))
    return coords


def get_coords2(univ: t.List[t.List[str]]) -> t.List[t.Tuple[int, int]]:
    coords = []
    for i in range(len(univ)):
        for j in range(len(univ[i])):
            if univ[i][j] == "#":
                coords.append(
                    (
                        i + [univ[x][j] for x in range(i)].count("E") * 999998,
                        j + univ[i][:j].count("E") * 999998,
                    )
                )
    return coords


def first_star(universe: t.List[t.List[str]]) -> int:
    coords = get_coords(expand(universe))
    count = 0
    for (x1, y1), (x2, y2) in list(itertools.combinations(coords, 2)):
        count += abs(x2 - x1) + abs(y2 - y1)
    return count


def second_star(universe: t.List[t.List[str]]) -> int:
    coords = get_coords2(expand2(universe))
    count = 0
    for (x1, y1), (x2, y2) in list(itertools.combinations(coords, 2)):
        count += abs(x2 - x1) + abs(y2 - y1)
    return count


print(first_star(universe))
print(second_star(universe))
