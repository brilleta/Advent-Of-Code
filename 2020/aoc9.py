from itertools import combinations
q = [int(i) for i in [line.rstrip() for line in open('aoc9.txt')]]

def findslice(target, maxind):
    for size in range(2, maxind):
        for k in range(0, maxind-size):
            if sum(q[k:k+size]) == target:
                return(min(q[k:k+size]) + max(q[k:k+size]))

for i in range(25,len(q)):
    if q[i] not in [a+b for a,b in combinations(q[i-25:i],2)]:
        print(f"Part 1: {q[i]} ({i}) is not a sum")
        print(f"Part 2: {findslice(q[i],i)}")
        break