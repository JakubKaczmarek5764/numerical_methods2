class Matrix():
    def __init__(self, m):
        self.m = m
    def solve(self):
        self.make_stairs()
        print(self.calc_x())
        self.print()

    def calc_x(self):
        x = []

    def make_stairs(self):
        for i in range(len(self.m)):
            if self.m[i][i] == 0: # sprawdza czy jest niezerowa wartosc i jezeli jest to zamienia wiersze
                self.swap_rows(self.m[i], self.m[self.find(i)])

            for j in range(i+1, len(self.m)):
                self.sub_row(self.m[j], self.m[i], self.m[j][i]/self.m[i][i])

        for i in range(len(self.m)):
            self.div_row(self.m[i], self.m[i][i])
    def print(self):
        print("")
        for row in self.m:
            print(row)
    def sub_row(self, r1, r2, mul=1):
        for i in range(len(r1)):
            r1[i] -= mul * r2[i]
    def swap_rows(self,r1,r2):
        for i in range(len(r1)):
            r1[i], r2[i] = r2[i], r1[i]
    def find(self, col):
        for i in range(len(self.m)):
            if self.m[i][col] != 0:
                return i
        return False
    def div_row(self, r1, div):
        for i in range(len(r1)):
            r1[i] /= div
# class Row():
#     def __init__(self,r):
#         self.r = r
#     def __sub__(self, other): # zakladamy, ze oba wiersze maja takie same dlugosci
#         copy = self.r[:]
#         for i in range(len(self.r)):
#             copy -= other.r[i]
#         return self
#     def __str__(self):
#         return list.__str__(self.r)