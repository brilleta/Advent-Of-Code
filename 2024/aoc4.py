input = open("/home/aurelien/BUAWEI/AOC/2024/aoc4.txt").read().splitlines()


def is_xmas(i: int, j: int, pattern: str) -> int:
    res = 0
    if (
        i + 3 < len(input)
        and input[i + 1][j] == pattern[0]
        and input[i + 2][j] == pattern[1]
        and input[i + 3][j] == pattern[2]
    ):
        res += 1
    if (
        i - 3 >= 0
        and input[i - 1][j] == pattern[0]
        and input[i - 2][j] == pattern[1]
        and input[i - 3][j] == pattern[2]
    ):
        res += 1
    if (
        j + 3 < len(input[i])
        and input[i][j + 1] == pattern[0]
        and input[i][j + 2] == pattern[1]
        and input[i][j + 3] == pattern[2]
    ):
        res += 1
    if (
        j - 3 >= 0
        and input[i][j - 1] == pattern[0]
        and input[i][j - 2] == pattern[1]
        and input[i][j - 3] == pattern[2]
    ):
        res += 1
    if (
        i + 3 < len(input)
        and j + 3 < len(input[i])
        and input[i + 1][j + 1] == pattern[0]
        and input[i + 2][j + 2] == pattern[1]
        and input[i + 3][j + 3] == pattern[2]
    ):
        res += 1
    if (
        i - 3 >= 0
        and j - 3 >= 0
        and input[i - 1][j - 1] == pattern[0]
        and input[i - 2][j - 2] == pattern[1]
        and input[i - 3][j - 3] == pattern[2]
    ):
        res += 1
    if (
        i - 3 >= 0
        and j + 3 < len(input[i])
        and input[i - 1][j + 1] == pattern[0]
        and input[i - 2][j + 2] == pattern[1]
        and input[i - 3][j + 3] == pattern[2]
    ):
        res += 1
    if (
        i + 3 < len(input)
        and j - 3 >= 0
        and input[i + 1][j - 1] == pattern[0]
        and input[i + 2][j - 2] == pattern[1]
        and input[i + 3][j - 3] == pattern[2]
    ):
        res += 1
    return res


def is_x_mas(i, j):
    return (
        i + 1 < len(input)
        and i - 1 >= 0
        and j + 1 < len(input[i])
        and j - 1 >= 0
        and (
            (
                input[i + 1][j + 1] == "S"
                and input[i - 1][j - 1] == "M"
                and input[i - 1][j + 1] == "S"
                and input[i + 1][j - 1] == "M"
            )
            or (
                input[i + 1][j + 1] == "M"
                and input[i - 1][j - 1] == "S"
                and input[i - 1][j + 1] == "M"
                and input[i + 1][j - 1] == "S"
            )
            or (
                input[i + 1][j + 1] == "M"
                and input[i - 1][j - 1] == "S"
                and input[i - 1][j + 1] == "S"
                and input[i + 1][j - 1] == "M"
            )
            or (
                input[i + 1][j + 1] == "S"
                and input[i - 1][j - 1] == "M"
                and input[i - 1][j + 1] == "M"
                and input[i + 1][j - 1] == "S"
            )
        )
    )


def first_star(input):
    res = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "X":
                res += is_xmas(i, j, "MAS")
            elif input[i][j] == "S":
                res += is_xmas(i, j, "AMX")
    return res / 2


def second_star(input: str) -> int:
    res = 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "A" and is_x_mas(i, j):
                res += 1
    return res


print(first_star(input))
print(second_star(input))
