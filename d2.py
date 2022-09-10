from d1 import Calculator

h = input("enter operation:")

if h.find ("+") !=-1:
    item = h.split("+")
    para1 = item[0]
    para2 = item[1]
    if item[0].find ("-") !=-1:
        minus = item[0].split("-")
        k = Calculator.subtract(int(item[1]) ,int(minus[1]))
        ad = []
        ad.append(int(minus[0]))
        ad.append(k)
        g = Calculator.add(ad)
    elif item[1].find ("-") !=-1:
        minus = item[1].split("-")
        ad = []
        ad.append(int(item[0]))
        ad.append(int(minus[0]))
        k = Calculator.add(ad)
        g = Calculator.subtract(k, int(minus[1]))
    else:
        ad = []
        b = 0
        while b < len(item):
            ad.append(int(item[b]))
            b += 1
        g = Calculator.add(ad)
    print(g)
    elif h.find ("-") !=-1:
    item=h.split ("-")
    num1 = item[0]
    num2 = item[1]
if item[0].find("+") != -1:
        add = item[0].split("+")
        m = Calculator.add(int(item[1]), int(add[1]))
        bb = []
        bb.append(int(add[0]))
        bb.append(m)
        p = Calculator.subtract(bb)
    elif item[1].find("+") != -1:
        add = item[1].split("+")
        bb = []
        bb.append(int(item[0]))
        bb.append(int(subtract[0]))
        p = Calculator.minus(bb)
        g = Calculator.subtract(p, int(add[1]))
    else:
        bb = []
        b = 0
    while b < len(item):
        bb.append(int(item[b]))
        b += 1
    v = Calculator.subtract(bb)
    print(v)
