lignes = open("/home/aurelien/AOC/2023/aoc1.txt").read().splitlines()

numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def get_num(word: str) -> int:
    num = ""
    for c in word:
        if c.isdigit():
            if len(num) >= 1:
                num = num[0] + c
            elif len(num) == 0:
                num = c + c
    return int(num)


def first_star(lines):
    return sum(get_num(line) for line in lines)


def get_first_digit_with_digits_in_words(word: str) -> int:
    w = ""
    for c in word:
        w += c
        if c.isdigit():
            return int(c)
        for i, n in enumerate(numbers):
            if n in w:
                return i + 1


def get_last_digit_with_digits_in_words(word: str) -> int:
    w = ""
    for c in word[::-1]:
        w += c
        if c.isdigit():
            return int(c)
        for i, n in enumerate(numbers):
            if n[::-1] in w:
                return i + 1


def second_star(lignes):
    res = 0
    for ligne in lignes:
        first = get_first_digit_with_digits_in_words(ligne)
        last = get_last_digit_with_digits_in_words(ligne)
        res += first * 10 + last
    return res


print(first_star(lignes))
print(second_star(lignes))
