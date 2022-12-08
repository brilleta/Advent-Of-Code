lignes = open("/home/aurelien/AOC/2021/aoc11-test.txt").read().splitlines()


class SquidGrid:
    def __init__(self, lignes) -> None:
        self.tab = []
        for ligne in lignes:
            self.tab.append([int(num) for num in ligne])

    def incr_energy_level(self):
        for i in range(self.tab):
            for j in range(self.tab[i]):
                self.tab[i][j] += 1

    def __str__(self) -> str:
        return str(self.tab)


print(str(SquidGrid(lignes)))
