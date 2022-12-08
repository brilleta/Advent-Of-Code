lignes = open("/home/aurelien/AOC/2021/aoc6.txt").read().splitlines()
poissons = lignes[0].split(",")
poissons = [int(v) for v in poissons]

res = {-1: 0, 0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

for poisson in poissons:
    res[poisson] += 1

poissons = res

for i in range(256):
    for i in range(10):
        if i == 0:
            poissons[9] += poissons[0]
            poissons[-1] = poissons[0]
            poissons[0] = 0
        else:
            poissons[i - 1] = poissons[i]
            poissons[i] = 0
    poissons[6] += poissons[-1]
    poissons[-1] = 0

print(sum(value for value in poissons.values()))
