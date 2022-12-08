lignes = open("/home/aurelien/AOC/2022/aoc2.txt").read().splitlines()

rpc = {"X": 1, "Y": 2, "Z": 3}
result1 = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3,
}

choose = {
    "AX": "Z",
    "AY": "X",
    "AZ": "Y",
    "BX": "X",
    "BY": "Y",
    "BZ": "Z",
    "CX": "Y",
    "CY": "Z",
    "CZ": "X",
}


def get_score(enemy: str, me: str):
    return rpc[me] + result1[enemy + me]


res = 0
for ligne in lignes:
    enemy, me = ligne.split(" ")
    res += get_score(enemy, me)

print(res)

res = 0
for ligne in lignes:
    enemy, me = ligne.split(" ")
    res += get_score(enemy, choose[enemy + me])

print(res)
