def opera(x, z):
    grade = "F"
    y = int(z)
    if y >= 70 and y <= 100:
        grade = "A"
    elif y >=60 and y <= 70:
        grade = "B"
    elif y >=50 and y < 60:
        grade = "c"
    elif y >= 45 and y < 50:
        grade = "D"
    elif y >= 40 and y < 44:
        grade = "E"
    elif y > 0 and y < 39:
        grade = "F"
    else:
        grade = "F"
    print(x + " got " + grade)
a = []
b = []
i = 0
while i < 5:
    in1 = input("Enter Name:")
    in2 = input("Enter Score:")
    a.append(in1)
    b.append(in2)
    i += 1
list(map(opera,a, b))



elif h.find("*") !=-1:
    item = h.split("*")
    h=int(eval(item[0])) * int(eval(item[1]))
    print(h)
elif h.find ("/") !=-1:
    item = h.split ("/")
    h = int(eval(item[0])) / int(eval(item[1]))
    print(h)
else:
    print("syntax error")



