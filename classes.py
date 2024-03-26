class Matrix():
    def __init__(self, m, precision=6):
        self.m = m
        self.precision = precision
    def solve(self):
        self.make_stairs()
        for i in range(len(self.m)):
            if round(self.m[i][i], self.precision) == 0:
                if round(self.m[-1][-1], self.precision) != 0:
                    return "Uklad sprzeczny"
                else:
                    return "Uklad nieoznaczony"
        return self.calc_x()[::-1]

    def calc_x(self):
        x = []
        for i in reversed(range(len(self.m))):
            tmpVal = self.m[i][-1]
            for j in range(len(self.m) - i - 1):
                tmpVal -= self.m[i][-j-2] * x[j]

            x.append(round(tmpVal/self.m[i][i], self.precision))
        return x
    def matrix_rank(self): # do zmiany
        val = 0
        for i in range(len(self.m)):
            if self.m[i][i] != 0:
                val+=1
        return val
    def make_stairs(self):
        for i in range(len(self.m)):
            to_swap = self.find(i)
            if to_swap != i: # wyznaczanie elementu glownego
                self.swap_rows(self.m[i], self.m[self.find(i)])
            if round(self.m[i][i],self.precision) == 0: continue
            for j in range(i+1, len(self.m)): # zera w kolejnych wierszach
                self.sub_row(self.m[j], self.m[i], self.m[j][i]/self.m[i][i])

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
        max = abs(self.m[col][col])
        max_index = col
        for i in range(col+1, len(self.m)):

            if abs(self.m[i][col]) > max:
                max = abs(self.m[i][col])
                max_index = i

        return max_index
    def div_row(self, r1, div):
        for i in range(len(r1)):
            r1[i] /= div