def get_row(s):
    down = 0
    up = 127
    for i in range(len(s)):
        if s[i] == 'B':
            down -= (down - up) // 2
        elif s[i] == 'F':
            up += (down - up) // 2
    if s[-1] == 'F':
        return down
    return up

def get_column(s):
    down = 0
    up = 7
    for i in range(len(s)):
        if s[i] == 'R':
            down -= (down - up) // 2
        elif s[i] == 'L':
            up += (down - up) // 2
    if s[-1] == 'L':
        return down
    return up

def get_seat_id(row, column):
    return row * 8 + column

assert(get_row("FBFBBFF") == 44)
assert(get_column("RLR") == 5)
assert(get_seat_id(get_row("BFFFBBF"), get_column("RRR")) == 567)
assert(get_seat_id(get_row("FFFBBBF"), get_column("RRR")) == 119)
assert(get_seat_id(get_row("BBFFBBF"), get_column("RLL")) == 820)


with open("/home/aurelien/AOC/aoc5.txt") as f:
    t = f.readlines()

tab = [x[:-1] for x in t]

seatIds = []
for boardpass in tab:
    seatIds.append(get_seat_id(get_row(boardpass[:-3]), get_column(boardpass[-3:])))
print(seatIds)


print(min(seatIds))
print(max(seatIds))

for i in range(min(seatIds), max(seatIds)):
    if i not in seatIds and i+1 in seatIds and i-1 in seatIds:
        print(i)