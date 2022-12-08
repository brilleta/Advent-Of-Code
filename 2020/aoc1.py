with open("/home/aurelien/AOC/aoc1.txt","r") as f:
    tabs = f.readlines();

def part1(tabs):
    for nombre1 in tabs:
        for nombre2 in tabs:
            n1 = int(nombre1)
            n2 = int(nombre2)
            if n1 > n2 and n1 + n2 == 2020:
                print(n1)
                print(n2)
                print(n1 + n2)
                print(n1 * n2)
                return n1 * n2
part1(tabs)

print("=================")

def part2(tabs):
    for nombre1 in tabs:
        for nombre2 in tabs:
            for nombre3 in tabs:
                n1 = int(nombre1)
                n2 = int(nombre2)
                n3 = int(nombre3)
                if n1 > n2 and n2 > n3 and n1 + n2 + n3 == 2020:
                    print(n1)
                    print(n2)
                    print(n3)
                    print(n1 + n2 + n3)
                    print(n1 * n2 * n3)
                    return n1 * n2 * n3

part2(tabs)