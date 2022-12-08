def tree_on_way(x, y, rd, tab):
    if y < len(tab)-1:
        mod = len(tab[y])
        return tab[y+rd[1]][(x+rd[0])%mod]=='#'
    return None

def count_trees(tab, rd):
    x = 0
    y = 0
    res = 0
    test = tree_on_way(x, y, rd, tab)
    while test is not None:
        if test:
            res += 1
        x += rd[0]
        y += rd[1]
        test = tree_on_way(x, y, rd, tab)
    return res

def part1(tab):
    return count_trees(tab, (3,1))

def part2(tab):
    rds = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    res = 1
    for rd in rds:
        res *= count_trees(tab, rd)
    return res

with open("/home/aurelien/AOC/aoc3.txt") as f:
    tab = f.readlines()

tab2 = [x[:-1] for x in tab]
print(part1(tab2))
print(part2(tab2))