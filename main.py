import classes
import input

obj = classes.Matrix([  # dobry
    [3,3,1,12],
    [2,5,7,33],
    [1,2,1,8]
])
print("Przyklad a \n"+str(obj.solve()))

obj = classes.Matrix([  # nieoznaczony
    [3,3,1,1],
    [2,5,7,20],
    [-4,-10,-14,-40]
])
print("Przyklad b \n"+str(obj.solve()))

obj = classes.Matrix([ # sprzeczny
    [3,3,1,1],
    [2,5,7,20],
    [-4,-10,-14,-20]
])
print("Przyklad c \n"+str(obj.solve()))

obj = classes.Matrix([ # dobry
    [0.5, -0.0625, 0.1875, 0.0625, 1.5],
    [-0.0625, 0.5, 0, 0, -1.625],
    [0.1875, 0, 0.375, 0.125, 1],
    [0.0625, 0, 0.125, 0.25, 0.4375]
])
print("Przyklad d \n"+str(obj.solve()))

obj = classes.Matrix([ # sprzeczny
    [3,2,1,-1,0],
    [5,-1,1,2,-4],
    [1,-1,1,2,4],
    [7,8,1,-7,6]
])
print("Przyklad e \n"+str(obj.solve()))

obj = classes.Matrix([ # dobry
    [3,-1,2,-1,-13],
    [3,-1,1,1,1],
    [1,2,-1,2,21],
    [-1,1,-2,-3,-5]
])
print("Przyklad f \n"+str(obj.solve()))

obj = classes.Matrix([  # dobry
    [0,0,1,3],
    [1,0,0,7],
    [0,1,0,5]
])
print("Przyklad g \n"+str(obj.solve()))

obj = classes.Matrix([  # dobry
    [10,-5,1,3],
    [4,-7,2,-4],
    [5,1,4,19]
])
print("Przyklad h \n"+str(obj.solve()))

obj = classes.Matrix([  # nieoznaczony
    [6,-4,2,4],
    [-5,5,2,11],
    [0.9,0.9,3.6,13.5]
])
print("Przyklad i \n"+str(obj.solve()))

obj = classes.Matrix([  # dobry
    [1,0.2,0.3,1.5],
    [0.1,1,-0.3,0.8],
    [-0.1,-0.2,1,0.7]
])
print("Przyklad j \n"+str(obj.solve()))

# obj = classes.Matrix(input.readfile("plik.txt"))
# print("Macierz z pliku \n"+str(obj.solve()))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
