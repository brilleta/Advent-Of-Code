lignes = open("/home/aurelien/AOC/2021/aoc1.txt").read().splitlines()

previous = None
counter = 0

for ligne in lignes:
    current = int(ligne)
    if previous is not None and current > previous:
        counter += 1
    previous = current

print(f"First answer : {counter}")

counter2 = 0

for i in range(len(lignes) - 3):
    if (int(lignes[i]) + int(lignes[i + 1]) + int(lignes[i + 2])) < (
        int(lignes[i + 1]) + int(lignes[i + 2]) + int(lignes[i + 3])
    ):
        counter2 += 1

print(f"Second part : {counter2}")
