from object import Results
a = []
for i in range(0, 2):
    inpn = input("Name:")
    inpt1 = int(input("Test1:"))
    inpt2 = int(input("Test2:"))
    inpex = int(input("Exam Score:"))
    b = Results(inpn,inpt1,inpt2,inpex)
    a.append(b)

i = 0
h = len(a)

while i < h:
    j = a[i].display()
    print(j)
    i = i + 1
