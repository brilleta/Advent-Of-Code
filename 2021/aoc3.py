from statistics import mode

lignes = open("/home/aurelien/AOC/2021/aoc3.txt").read().splitlines()

gamma = ""

for i in range(len(lignes[0])):
    gamma += mode([ligne[i] for ligne in lignes])


def reverse_bytes(byte):
    res = ""
    for bit in byte:
        if bit == "0":
            res += "1"
        else:
            res += "0"
    return res


print(gamma)
epsilon = reverse_bytes(gamma)
print(epsilon)

print(int(gamma, 2) * int(epsilon, 2))


def present_elements(list, mode):
    if len(list) > 1:
        count0 = 0
        count1 = 0
        for element in list:
            if element == "0":
                count0 += 1
            else:
                count1 += 1

        if count0 == count1:
            return "1" if mode == "most" else "0"
        elif count0 > count1:
            return "0" if mode == "most" else "1"
        else:
            return "1" if mode == "most" else "0"
    return ""


o2 = ""
co2 = ""

for i in range(len(lignes[0])):
    o2 += present_elements(
        [ligne[i] for ligne in lignes if ligne.startswith(o2)], "most"
    )
    co2 += present_elements(
        [ligne[i] for ligne in lignes if ligne.startswith(co2)], "less"
    )
    print(o2 + "\n")
    print(co2 + "\n")

o2 = next(ligne for ligne in lignes if ligne.startswith(o2))
co2 = next(ligne for ligne in lignes if ligne.startswith(co2))
print(o2)
print(co2)

print(int(o2, 2) * int(co2, 2))
