import string

lines = open("/home/aurelien/AOC/2023/aoc3.txt").read().splitlines()

symbols = list(string.punctuation)
symbols.remove(".")

directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 0),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def symbols_around(i, j, engine):
    max_x, max_y = len(engine), len(engine[i])
    for x, y in directions:
        if (
            i + x < max_x
            and j + y < max_y
            and i + x >= 0
            and j + y >= 0
            and engine[i + x][j + y] in symbols
        ):
            return True
    return False


def first_star(lines):
    engine = [[c for c in line] for line in lines]
    count = 0
    conform = False
    current_number = ""
    for i in range(len(engine)):
        for j in range(len(engine[i])):
            if engine[i][j].isdigit():
                current_number += engine[i][j]
                conform = symbols_around(i, j, engine) or conform
            else:
                if conform:
                    count += int(current_number)
                current_number = ""
                conform = False
        if conform:
            count += int(current_number)
        current_number = ""
        conform = False
    return count


def gear_around(i, j, engine):
    max_x, max_y = len(engine), len(engine[i])
    for x, y in directions:
        if (
            i + x < max_x
            and j + y < max_y
            and i + x >= 0
            and j + y >= 0
            and engine[i + x][j + y] == "*"
        ):
            return i + x, j + y
    return None, None


def second_star(lines):
    engine = [[c for c in line] for line in lines]
    gear_x = None
    gear_y = None
    current_number = ""
    gears = {}
    for i in range(len(engine)):
        for j in range(len(engine[i])):
            if engine[i][j].isdigit():
                current_number += engine[i][j]
                x, y = gear_around(i, j, engine)
                gear_x, gear_y = (
                    (x, y) if x is not None and y is not None else (gear_x, gear_y)
                )
            else:
                if gear_x is not None and gear_y is not None:
                    c_id = "x" + str(gear_x) + "y" + str(gear_y)
                    if c_id in gears:
                        gears[c_id]["count"] += 1
                        gears[c_id]["num"] *= int(current_number)
                    else:
                        gears[c_id] = {"count": 1, "num": int(current_number)}
                current_number = ""
                gear_x = None
                gear_y = None
        if gear_x is not None and gear_y is not None:
            c_id = "x" + str(gear_x) + "y" + str(gear_y)
            if c_id in gears:
                gears[c_id]["count"] += 1
                gears[c_id]["num"] *= int(current_number)
            else:
                gears[c_id] = {"count": 1, "num": int(current_number)}
        current_number = ""
        gear_x = None
        gear_y = None
    return sum(x["num"] for x in gears.values() if x["count"] == 2)


# 925
print(first_star(lines))
print(second_star(lines))
