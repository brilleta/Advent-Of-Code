lignes = open("/home/aurelien/AOC/2021/aoc10.txt").read().splitlines()

table = {")": 3, "]": 57, "}": 1197, ">": 25137}
table2 = {"(": 1, "[": 2, "{": 3, "<": 4}
equivalent = {"(": ")", "{": "}", "<": ">", "[": "]"}


def well_written(word):
    res = 0
    queue = []
    for letter in word:
        if letter in ["(", "[", "{", "<"]:
            queue.append(letter)
        else:
            if letter != equivalent[queue[-1]]:
                res = table[letter]
                break
            else:
                queue.pop()
    return res


total = 0
for ligne in lignes:
    total += well_written(ligne)

print(total)


def well_written(word):
    queue = []
    for letter in word:
        if letter in ["(", "[", "{", "<"]:
            queue.append(letter)
        else:
            if letter != equivalent[queue[-1]]:
                return None
            else:
                queue.pop()
    return queue


def calculate_score(queue):
    total = 0
    queue.reverse()
    for letter in queue:
        total = total * 5 + table2[letter]
    return total


totals = []

for ligne in lignes:
    queue = well_written(ligne)
    if queue is not None and len(queue) != 0:
        totals.append(calculate_score(queue))

print(sorted(totals)[len(totals) // 2])
