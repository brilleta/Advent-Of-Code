lignes = open("/home/aurelien/AOC/2021/aoc8.txt").read().splitlines()

res = 0

for ligne in lignes:
    ligne = ligne.split(" | ")[1]
    for value in ligne.split():
        if len(value) in [2, 4, 3, 7]:
            res += 1
print(res)


outputs = []


def supperpose(value1, value2):
    res = 0
    for l in value1:
        if l in value2:
            res += 1
    return res


def get_key(value, dict):
    for key, v in dict.items():
        if v == value:
            return key


def decode(values):
    res = {0: "", 1: "", 2: "", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: ""}
    for value in values:
        value = "".join(sorted(value))
        if len(value) == 2:
            res[1] = value
        elif len(value) == 3:
            res[7] = value
        elif len(value) == 4:
            res[4] = value
        elif len(value) == 7:
            res[8] = value
    for value in values:
        value = "".join(sorted(value))
        if len(value) == 5:
            if supperpose(value, res[4]) == 2:
                res[2] = value
            else:
                if supperpose(value, res[1]) == 2:
                    res[3] = value
                else:
                    res[5] = value
        elif len(value) == 6:
            if supperpose(value, res[4]) == 4:
                res[9] = value
            else:
                if supperpose(value, res[1]) == 2:
                    res[0] = value
                else:
                    res[6] = value
    return res


def decode_nums(ligne):
    parts = ligne.split(" | ")
    part1 = parts[0].split()
    part2 = parts[1].split()

    dict_num = decode(part1)
    print(dict_num)
    res = ""

    for part in part2:
        res += str(get_key("".join(sorted(part)), dict_num))

    return int(res)


total = 0
for ligne in lignes:
    total += decode_nums(ligne)

print(total)
