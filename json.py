def opera(z):
    grade = "F"
    y = z
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
    return grade

a=[]
b=[]
c=[]
d=[]
e= []
r = 0
while r <= 4:
    h=input("Enter your name:")
    i=int(input("Enter 1st test score:"))
    j = int(input("Enter 2nd test score:"))
    k = int(input("Enter exam score:"))

    a.append(h)
    b.append(i)
    c.append(j)
    d.append(k)
    v=i+j+k
    e.append(v)
    r += 1

grade = list(map(opera, e))

u = "name   " + "Test1   " + "Test2    " + "Exam   " + "total    " + "grade    "
print(u)
x = len(a)
for i in range(0,x):
    print(str(a[i]) + "-----" + str(b[i]) + "-----" + str(c[i]) + "-----" + str(d[i]) + "-----" + str(e[i]) + "-----" + str(grade[i]))
