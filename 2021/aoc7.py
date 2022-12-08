lignes = open("/home/aurelien/AOC/2021/aoc7.txt").read().splitlines()
positions = lignes[0].split(",")
positions = [int(v) for v in positions]

res = []
temp = 0

for i in range(max(positions)):
    for j in range(len(positions)):
        temp += abs(positions[j] - i)
    res.append(temp)
    temp = 0

print(min(res))

res2 = []
temp2 = 0

for i in range(max(positions)):
    for j in range(len(positions)):
        diff = abs(positions[j] - i)
        temp2 += diff * (diff + 1) // 2
    res2.append(temp2)
    temp2 = 0

print(min(res2))
