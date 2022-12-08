lignes = open("/home/aurelien/AOC/2022/aoc5.txt").read().splitlines()
pile = [
    "VRHBGDW",
    "FRCGNJ",
    "JNDHFSL",
    "VSDJ",
    "VNWQRDHS",
    "MCHGP",
    "CHZLGBJF",
    "RJS",
    "MVNBRSGL",
]

pile_test = ["NZ", "DCM", "P"]

pile = [list(x[::-1]) for x in pile]
pile_test = [list(x[::-1]) for x in pile_test]

pile1 = pile.copy()
pile2 = pile.copy()

for ligne in lignes:
    ligne = ligne.split(" ")
    steps = int(ligne[1])
    from_ = int(ligne[3]) - 1
    to = int(ligne[5]) - 1
    for _ in range(steps):
        x = pile1[from_].pop()
        pile1[to].append(x)

res = "".join([x[-1] for x in pile1])
print(res)


for ligne in lignes:
    ligne = ligne.split(" ")
    steps = int(ligne[1])
    from_ = int(ligne[3]) - 1
    to = int(ligne[5]) - 1
    l = []
    for _ in range(steps):
        x = pile2[from_].pop()
        l.append(x)
    l.reverse()
    [pile2[to].append(x) for x in l]

res2 = "".join([x[-1] for x in pile2])
print(res2)
