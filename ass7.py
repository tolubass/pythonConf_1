names=[]

a = input("Enter first name:")
x1 = input("Enter fist score:")
b = input("Enter second name:")
x2 = input("Enter second score:")
c = input("Enter third name:")
x3 = input("Enter third score:")
d = input("Enter fourth name:")
x4 = input("Enter fourth score:")
e = input("Enter fifth name:")
x5 = input("Enter fifth score:")
f = input("Enter sixth name:")
x6 = input("Enter sixth score:")
l=(a,b,c,d,e,f)
v=(x1, x2, x3, x4, x5, x6)
total = len(names)
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
list(map(opera,(l), (v)))







