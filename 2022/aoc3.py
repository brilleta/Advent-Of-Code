lignes = open("/home/aurelien/AOC/2022/aoc3.txt").read().splitlines()


def get_priority(letter):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letters.index(letter) + 1


def get_same_letter(w1, w2):
    return "".join(set(w1).intersection(w2))


def get_same_letter2(w1, w2, w3):
    return list(set(w1) & set(w2) & set(w3))[0]


res = 0

for ligne in lignes:
    firstpart, secondpart = ligne[: int(len(ligne) / 2)], ligne[int(len(ligne) / 2) :]
    res += get_priority(get_same_letter(firstpart, secondpart))

print(res)


res = 0
temp = []
for ligne in lignes:
    temp.append(ligne)
    if len(temp) == 3:
        res += get_priority(get_same_letter2(temp[0], temp[1], temp[2]))
        temp = []

print(res)
