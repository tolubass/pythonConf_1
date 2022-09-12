#months
a =['january','febuary', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october','november','december']
b =[31,28,31,30,31,30,31,31,30,31,30,31]
for i in range (1,13):
    h = input("search month days:")
    if h==a[0]:
        print(f"it has " + str(b[0]) + " days")
    elif h==a[1]:
        print(f"it has " + str(b[1]) + " days")
    elif h==a[2]:
        print(f"it has " + str(b[2]) + " days")
    elif h==a[3]:
        print(f"it has " + str(b[3]) + " days")
    elif h==a[4]:
        print(f"it has " + str(b[4]) + " days")
    elif h==a[5]:
        print(f"it has " + str(b[5]) + " days")
    elif h==a[6]:
        print(f"it has " + str(b[6]) + " days")
    elif h==a[7]:
        print(f"it has " + str(b[7]) + " days")
    elif h==a[8]:
        print(f"it has " + str(b[8]) + " days")
    elif h==a[9]:
        print(f"it has " + str(b[9]) + " days")
    elif h==a[10]:
        print(f"it has " + str(b[10]) + " days")
    elif h==a[11]:
        print(f"it has " + str(b[11]) + " days")
    elif h==a[12]:
        print(f"it has " + str(b[12]) + " days")
    elif h!=a:
        print("month doesnt exist")
    else:
        print("month doesnt exist")
