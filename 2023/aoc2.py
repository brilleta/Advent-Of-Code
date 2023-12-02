lines = open("/home/aurelien/AOC/2023/aoc2.txt").read().splitlines()


def first_star(lines):
    res = 0
    for i, line in enumerate(lines):
        games = line.split(":")[1]
        possible = True
        for game in games.split(";"):
            for ball in game.split(","):
                num = int(ball[:3])
                color = ball[3:].strip()
                if color == "red" and num > 12:
                    possible = False
                    break
                elif color == "green" and num > 13:
                    possible = False
                    break
                elif color == "blue" and num > 14:
                    possible = False
                    break
            if not possible:
                break
        if possible:
            print(games)
            res += i + 1
    return res


def first_star(lines):
    res = 0
    for i, line in enumerate(lines):
        games = line.split(":")[1]
        red = 0
        green = 0
        blue = 0
        for game in games.split(";"):
            for ball in game.split(","):
                num = int(ball[:3])
                color = ball[3:].strip()
                if color == "red":
                    red = num if num > red else red
                elif color == "green":
                    green = num if num > green else green
                elif color == "blue":
                    blue = num if num > blue else blue

        res += red * blue * green
    return res


print(first_star(lines))
