def manage_line_part1(line):
    nb, lettre, mot = line.split(' ')
    lettre = lettre[0]
    nbmin, nbmax = nb.split('-')
    occur = mot.count(lettre)
    return occur >= int(nbmin) and occur <= int(nbmax)

def manage_line_part2(line):
    nb, lettre, mot = line.split(' ')
    lettre = lettre[0]
    nbmin, nbmax = nb.split('-')
    return (mot[int(nbmin)-1] == lettre) != (mot[int(nbmax)-1] == lettre)

assert manage_line_part1("1-3 a: abcde")==True
assert manage_line_part1("1-3 b: cdefg")==False
assert manage_line_part1("2-9 c: ccccccccc")==True

assert manage_line_part2("1-3 a: abcde")==True
assert manage_line_part2("1-3 b: cdefg")==False
assert manage_line_part2("2-9 c: ccccccccc")==False

with open("/home/aurelien/AOC/aoc2.txt") as f:
    lignes = f.readlines()
lignes.pop()
i=0
j=0
for l in lignes:
    if manage_line_part1(l):
        i+=1
    if manage_line_part2(l):
        j+=1
print(f"Résultat part 1: {i}\n Résultat part 2: {j}")
