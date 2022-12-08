lines = open("/home/aurelien/AOC/2022/aoc6.txt").read().splitlines()

marker = set()
for line in lines:
    for i in range(len(line)):
        for j in range(4):
            marker.add(line[i + j])
        if len(marker) == 4:
            print(i + 4)
            break
        else:
            marker = set()

marker = set()
for line in lines:
    for i in range(len(line)):
        for j in range(14):
            marker.add(line[i + j])
        if len(marker) == 14:
            print(i + 14)
            break
        else:
            marker = set()
