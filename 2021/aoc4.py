lignes = open("/home/aurelien/AOC/2021/aoc4.txt").read().splitlines()


class Bingo:
    def __init__(self, lignes):
        self.tab = []
        self.finish = False
        for ligne in range(len(lignes)):
            self.tab.append([])
            for col in lignes[ligne].split():
                self.tab[ligne].append([int(col), False])

    def get_score(self):
        return sum([sum([i[0] for i in t if not i[1]]) for t in self.tab])

    def check_num(self, num):
        for i in range(len(self.tab)):
            for j in range(len(self.tab[i])):
                if self.tab[i][j][0] == num:
                    self.tab[i][j][1] = True
                    return

    def check_col_win(self, col):
        return all(self.tab[i][col][1] for i in range(len(self.tab)))

    def check_lig_win(self, ligne):
        return all(elmt[1] for elmt in self.tab[ligne])

    def check_win(self):
        if not self.finish:
            res = any(self.check_col_win(i) for i in range(len(self.tab[0]))) or any(
                self.check_lig_win(j) for j in range(len(self.tab))
            )
            if res:
                self.finish = True
            return res
        return True


b = Bingo([lignes[i] for i in range(2, 6)])
print(b.tab)
b.tab[0][0][1] = True
print(b.get_score())
print(b.check_win())
nums = lignes[0].split(",")
bingos = []
bingo = []

for i in range(2, len(lignes)):
    if lignes[i] != "":
        bingo.append(lignes[i])
    else:
        bingos.append(Bingo(bingo))
        bingo = []
bingos.append(Bingo(bingo))
print(nums)
print(len(bingos))


def play(nums, bingos):
    res = []
    for num in nums:
        for bingo in bingos:
            if not bingo.finish:
                bingo.check_num(int(num))
                if bingo.check_win():
                    res.append(bingo.get_score() * int(num))
                    print(bingo.tab, num)
    return res


results = play(nums, bingos)
print(len(results))
print(results[0])
print(results[-1])
print(results)
