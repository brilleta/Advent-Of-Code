lines = open("/home/aurelien/AOC/2022/aoc8.txt").read().splitlines()
forest = [[int(x) for x in list(line)] for line in lines]
width = len(forest[0])
height = len(forest)


def is_visible(x, y):
    value = forest[x][y]
    if x + 1 >= width or y + 1 >= height or y - 1 < 0 or x - 1 < 0:
        return True
    return (
        all(value > forest[x][i] for i in range(y))
        or all(value > forest[x][i] for i in range(y + 1, height))
        or all(value > forest[i][y] for i in range(x))
        or all(value > forest[i][y] for i in range(x + 1, width))
    )


def scenic_score(x, y):
    value = forest[x][y]
    a = 0
    b = 0
    c = 0
    d = 0
    for i in range(y - 1, -1, -1):
        a += 1
        if value <= forest[x][i]:
            break
    for i in range(y + 1, height):
        b += 1
        if value <= forest[x][i]:
            break
    for i in range(x - 1, -1, -1):
        c += 1
        if value <= forest[i][y]:
            break
    for i in range(x + 1, width):
        d += 1
        if value <= forest[i][y]:
            break
    return a * b * c * d


res = 0
res2 = []
for x in range(width):
    for y in range(height):
        if is_visible(x, y):
            res += 1
        score = scenic_score(x, y)
        res2.append(score)

print(res)
print(max(res2))
