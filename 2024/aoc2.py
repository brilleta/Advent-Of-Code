lignes = open("/home/aurelien/BUAWEI/AOC/2024/aoc2.txt").read().splitlines()


def is_safe(numbers: list[int]):
    for i in range(len(numbers) - 1):
        if i == 0:
            increasing = numbers[i] <= numbers[i + 1]
        if increasing != (numbers[i] <= numbers[i + 1]):
            return False
        if abs(numbers[i] - numbers[i + 1]) > 3 or numbers[i] - numbers[i + 1] == 0:
            return False

    return True


def first_star(lines):
    count = 0
    for line in lines:
        numbers = [int(x) for x in line.split(" ")]
        if is_safe(numbers):
            count += 1
    return count


def second_star(lines):
    count = 0
    for line in lines:
        numbers = [int(x) for x in line.split(" ")]
        if is_safe(numbers):
            count += 1
        else:
            for i in range(len(numbers)):
                if is_safe([x for index, x in enumerate(numbers) if index != i]):
                    count += 1
                    break
    return count


print(first_star(lignes))
print(second_star(lignes))
