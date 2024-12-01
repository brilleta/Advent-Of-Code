lignes = open("/home/aurelien/BUAWEI/AOC/2024/aoc1.txt").read().splitlines()

l1 = sorted(int(ligne.split("   ")[0]) for ligne in lignes)
l2 = sorted(int(ligne.split("   ")[1]) for ligne in lignes)


def first_star(l1, l2):
    return sum(abs(a - b) for a, b in zip(l1, l2))


def second_star(l1, l2):
    return sum(a * l2.count(a) for a in l1)


print(first_star(l1, l2))
print(second_star(l1, l2))
