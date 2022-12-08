lignes = open("/home/aurelien/AOC/2022/aoc1.txt").read().splitlines()
elfs = [0]
for ligne in lignes:
    if ligne == "":
        elfs.append(0)
    else:
        elfs[-1] += int(ligne)

elfs_sorted = sorted(elfs)

res1 = elfs_sorted[-1]
print(res1)

res2 = sum(elfs_sorted[-3:])
print(res2)
