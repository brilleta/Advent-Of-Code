import re

input = open("/home/aurelien/BUAWEI/AOC/2024/aoc3.txt").read()


def find_mul(input: str):
    return re.findall(r"mul\(\d+,\d+\)", input)


def find_mul_do_dont(input: str):
    return re.findall(r"don't\(\)|do\(\)|mul\(\d+,\d+\)", input)


def first_star(input: str):
    mults = find_mul(input)
    res = 0
    for mult in mults:
        a, b = mult.replace("mul(", "").replace(")", "").split(",")
        res += int(a) * int(b)
    return res


def second_star(input):
    mults = find_mul_do_dont(input)
    print(mults)
    res = 0
    do = True
    for mult in mults:
        if "mul" in mult and do:
            a, b = mult.replace("mul(", "").replace(")", "").split(",")
            res += int(a) * int(b)
            do = True
        elif "do()" == mult:
            do = True
        elif "don't()" == mult:
            do = False
    return res


# print(first_star(input))
print(second_star(input))
