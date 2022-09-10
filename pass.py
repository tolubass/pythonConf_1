print("pass pass pass pass")
a=input("enter first number:")
b=input("enter second number")
total = 0
try:
    c = int(a)
    d = int(b)
except ValueError as p:
    pass
else:
    total = c+d
    print(f"total is: {total}")
    print("the program completes successfully")


