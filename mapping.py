
def opera(x,y):
    grade = "F"
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
    print (x + " got " + grade)
list(map(opera,("ojo", "olu", "rex", "bayo", "ope", "yomi"), (31, 41, 51, 61, 71, 81)))

