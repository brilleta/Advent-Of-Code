lignes = open("/home/aurelien/AOC/2021/aoc2.txt").read().splitlines()

horizontal = 0
profondeur = 0
aim = 0
for ligne in lignes:
    mode = ligne.split()[0]
    step = int(ligne.split()[1])
    if mode == "forward":
        profondeur += aim * step
        horizontal += step
    elif mode == "up":
        aim -= step
    elif mode == "down":
        aim += step

print(f"Answer : {horizontal * profondeur}")
