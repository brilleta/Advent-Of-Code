lignes = open("/home/aurelien/AOC/2021/aoc5.txt").read().splitlines()

tab = []
taille = 1000
for i in range(taille):
    tab.append([0 for _ in range(taille)])

for ligne in lignes:
    s = ligne.split(" -> ")
    y1 = int(s[0].split(",")[0])
    x1 = int(s[0].split(",")[1])
    y2 = int(s[1].split(",")[0])
    x2 = int(s[1].split(",")[1])
    if x1 == x2:
        min_y = min(y1, y2)
        for i in range(abs(y2 - y1) + 1):
            if min_y + i < taille:
                tab[x1][min_y + i] += 1
    elif y1 == y2:
        min_x = min(x1, x2)
        for j in range(abs(x2 - x1) + 1):
            if min_x + j < taille:
                tab[min_x + j][y1] += 1
    elif x1 < x2 and y1 < y2:
        for k in range(abs(y2 - y1) + 1):
            tab[x1 + k][y1 + k] += 1
    elif x1 > x2 and y1 < y2:
        for k in range(abs(x2 - x1) + 1):
            tab[x1 - k][y1 + k] += 1
    elif x1 < x2 and y1 > y2:
        for k in range(abs(y2 - y1) + 1):
            tab[x1 + k][y1 - k] += 1
    elif x1 > x2 and y1 > y2:
        for k in range(abs(x2 - x1) + 1):
            tab[x1 - k][y1 - k] += 1

count = 0
for i in range(taille):
    for j in range(taille):
        if tab[i][j] > 1:
            count += 1

for i in range(len(tab)):
    print(str(tab[i]) + "\n")
print(count)
