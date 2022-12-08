def part1(tab):
    ens = set()
    res = 0
    for ligne in tab:
        if ligne == "":
            res += len(ens)
            ens.clear()
        else:
            ens = ens | set(ligne)
    return res

def part2(tab):
    ens = set()
    res = 0
    for ligne in tab:
        if ligne == "":
            res += len(ens)
            ens.clear()
        else:
            ens = ens & set(ligne)
    return res

assert(part1(["abc","","a","b","c","","ab","ac","","a","a","a","a","","b",""]) == 11)
with open("/home/aurelien/AOC/aoc6.txt") as f:
    t = f.readlines()

tab = [x[:-1] for x in t]
print(part1(tab))
print(part2(tab))
