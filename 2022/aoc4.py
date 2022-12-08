lignes = open("/home/aurelien/AOC/2022/aoc4.txt").read().splitlines()


def contains_section(s1, s2):
    s1_start, s1_end = s1.split("-")
    s2_start, s2_end = s2.split("-")
    s1_start = int(s1_start)
    s1_end = int(s1_end)
    s2_start = int(s2_start)
    s2_end = int(s2_end)
    return (s1_start >= s2_start and s1_end <= s2_end) or (
        s2_start >= s1_start and s2_end <= s1_end
    )


def overlap(s1, s2):
    s1_start, s1_end = s1.split("-")
    s2_start, s2_end = s2.split("-")
    s1_start = int(s1_start)
    s1_end = int(s1_end)
    s2_start = int(s2_start)
    s2_end = int(s2_end)
    return (
        len(set(range(s1_start, s1_end + 1)).intersection(range(s2_start, s2_end + 1)))
        > 0
    )


res = 0

for ligne in lignes:
    section1, section2 = ligne.split(",")
    res += 1 if contains_section(section1, section2) else 0

print(res)

res = 0

for ligne in lignes:
    section1, section2 = ligne.split(",")
    res += 1 if overlap(section1, section2) else 0

print(res)
