i=input(" enter gmail: ")
a = "@gmail.com"
b = "@yahoo.com"
c = "@inbox.com"
if i.find("@gmail.com") != -1:
    print(i)
elif i.find("@yahoo.com") != -1:
    print(i)
elif i.find("@inbox.com") != -1:
    print(i)
else:
    print("invalid email")

