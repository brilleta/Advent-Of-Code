import typing as t

lines = open("/home/aurelien/AOC/2023/aoc9.txt").read().splitlines()

sequences = [[int(x) for x in line.strip().split(" ")] for line in lines]


def extrapolated(sequence: t.List[int]) -> int:
    if set(sequence) == {0}:
        return 0
    return sequence[-1] + extrapolated(
        [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
    )


def extrapolated2(sequence: t.List[int]) -> int:
    print(sequence)
    if set(sequence) == {0}:
        return 0
    return sequence[0] - extrapolated2(
        [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
    )


def first_star(sequences: t.List[t.List[int]]) -> int:
    return sum(extrapolated(s) for s in sequences)


def second_star(sequences: t.List[t.List[int]]) -> int:
    return sum(extrapolated2(s) for s in sequences)


print(first_star(sequences))
print(second_star(sequences))
