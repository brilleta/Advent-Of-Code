def is_present(d):
    rules = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    res = True
    if len(d) > len(rules)+1 or len(d)<len(rules):
        return False
    for r in rules:
        if r not in d.keys():
            res = False
            break
    return res

assert(is_present({"ecl":"gry", "pid":"860033327", "eyr":"2020", "hcl":"#fffffd", "byr":"1937", "iyr":"2017", "cid":"147", "hgt":"183cm"})==True)

assert(is_present({"iyr":"2013", "ecl":"amb", "cid":"350", "eyr":"2023", "pid":"028048884", "hcl":"#cfa07d", "byr":"1929"}) == False)
"""
hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

def is_valid(key, value):
    if key == "byr":
        return len(value) == 4 and value.isdigit() and 1920 <= int(value) <= 2002
    elif key == "iyr":
        return len(value) == 4 and value.isdigit() and 2010 <= int(value) <= 2020
    elif key == "eyr":
        return len(value) == 4 and value.isdigit() and 2020 <= int(value) <= 2030
    elif key == "hgt":
        if value.endswith('cm'):
            number = value[:-2]
            return number.isdigit() and 150 <= int(number) <= 193

        elif value.endswith('in'):
            number = value[:-2]
            return number.isdigit() and 59 <= int(number) <= 76
        else:
            return False

    elif key == "hcl":
        return len(value) == 7 and value[0] == '#' and all(c in "0123456789abcdef" for c in value[1:])
    elif key == "ecl":
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif key == "pid":
        return len(value) == 9 and value.isdigit()
    return True

def count_valids(tab):
    d = {}
    count = 0
    for ligne in tab:
        if ligne == "":
            if is_present(d) and all(is_valid(key, value) for key, value in d.items()):
                count += 1
            d = {}
        else:
            mots = ligne.split(" ")
            for mot in mots:
                cle, valeur = mot.split(":")
                d[cle] = valeur
    return count



with open("/home/aurelien/AOC/aoc4.txt") as f:
    t = f.readlines()

tab = [x[:-1] for x in t]
print(count_valids(tab))