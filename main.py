# This is a sample Python script.
import classes


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
t1 = [1,2,3]
t2 = [1,2,3]

obj = classes.Matrix([ # dobry
    [3,-1,2,-1,-13],
    [3,-1,1,1,1],
    [1,2,-1,2,21],
    [-1,1,-2,-3,-5]
])
print(obj.solve())

obj = classes.Matrix([ # nieoznaczony
    [3,3,1,1],
    [2,5,7,20],
    [-4,-10,-14,-40]
])
print(obj.solve())
obj = classes.Matrix([ # sprzeczny
    [3,3,1,1],
    [2,5,7,20],
    [-4,-10,-14,-20]
])
print(obj.solve())

obj = classes.Matrix([ # dobry
    [0.5, -0.0625, 0.1875, 0.0625, 1.5],
    [-0.0625, 0.5, 0, 0, -1.625],
    [0.1875, 0, 0.375, 0.125, 1],
    [0.0625, 0, 0.125, 0.25, 0.4375]
])
print(obj.solve())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
