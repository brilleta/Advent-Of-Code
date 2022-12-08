import numpy

lignes = open("/home/aurelien/AOC/2021/aoc9.txt").read().splitlines()

tab = []

for ligne in lignes:
    tab.append([int(num) for num in ligne])

bound_x = len(tab[0])
bound_y = len(tab)

res = 0

for i in range(bound_y):
    for j in range(bound_x):
        test = []
        if j + 1 < bound_x:
            test.append(tab[i][j] < tab[i][j + 1])
        if j - 1 >= 0:
            test.append(tab[i][j] < tab[i][j - 1])
        if i + 1 < bound_y:
            test.append(tab[i][j] < tab[i + 1][j])
        if i - 1 >= 0:
            test.append(tab[i][j] < tab[i - 1][j])
        if all(test):
            res += tab[i][j] + 1

print(res)


def basin_length(tab, x, y, checked):
    if (
        (x, y) in checked
        or x < 0
        or y < 0
        or x >= bound_x
        or y >= bound_y
        or tab[y][x] == 9
    ):
        return 0
    checked.append((x, y))
    return (
        1
        + basin_length(tab, x + 1, y, checked)
        + basin_length(tab, x - 1, y, checked)
        + basin_length(tab, x, y + 1, checked)
        + basin_length(tab, x, y - 1, checked)
    )


bassins = set()

for y in range(bound_y):
    for x in range(bound_x):
        num = tab[i][j]
        if num != 9:
            total = 0
            total += basin_length(tab, x, y, [])
            bassins.add(total)

print(bassins)
results = sorted(list(bassins))[-3:]
print(results)
print(numpy.prod(results))
