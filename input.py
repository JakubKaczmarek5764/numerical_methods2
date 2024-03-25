def readfile(name):
    tmpArr = []
    f = open(name, 'r')
    for line in f:
        tmpArr.append([float(x) for x in line.split(" ")])
    f.close()
    return tmpArr