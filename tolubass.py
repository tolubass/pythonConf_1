

a="2"
b=1
c=int(a)
x=b+c
print(x)





n=['tolu','daniel','bola','yuriel','zainab','ayo','tobi','ike','rex','gbenga','ope','kemi','seyi','mike','eli']
n.sort()
print(n)
n.remove('bola')
print(n)
n.insert(1,'bola')
print(n)

a=70
b=65
c=95
d=45
e=40
x=a+b+c+d+e
y=5
avg=x/y
print(avg)
if a>=70 and a<=100:
    print("your grade is A")
elif a>=61 and a<70:
    print("your grade is B")
elif a>=51 and a<60:
    print("your grade is C")
elif a>=45 and a<50:
    print("your grade is D")
elif a>=40 and a<44:
    print("your grade is E")
elif a>=0 and a<39:
    print("your grade is F")
else:
    print("unknown result")


g = {"name":"Bola Ojo","age": 23, "isAdmin": True, "State Of Origin":"Osun State"}
a = g["name"]
if g["isAdmin"] == False:
    print(a)


pin=2001
p=pin
if p ==2002:
    print(p)
elif p==2002:
    print(p)
elif p==2003:
    print(p)
elif p==1959:
    print(p)
elif p==2001:
    print(p)
else:
    print("incorrect pin")


h={}
h["pin"]="2545"
h["occupation"]="student"
h["country"]="germany"
h["location"]="ado"
h["sex"]="male"
print(h)
d=h["sex"]
print(d)
d=h["location"]
print(d)

ATM=60000
a=ATM
if a==10000:
    print("10000")
elif a>10000:
    print("maximum is 10,000")
else:
    print("incorrect pin!")


p=[2,4,5,6]
y=[4,5,7,9]
x=p[3]
print(x)


l=0.0002
if l==0.01:
    print("buy")
elif l<0.01:
    print("not possible pls")
elif l<=0.5:
    print("buy")
else:
    print("not enough money")


student={"name":"john", "age":25, "course":"microbiology"}
student ["phone"] = "08101072847"
student["occupation"] = "doctor"
student.update ({"name":"tolu", "age":26})
del student["age"]
print(student)






i=400
while i>=1:
    print(i)
    i-=1



a= {"State":"Ondo State","country":"Nigeria", "Details":[
    {"user": "odun3","pass": "mypascode","email": "odun@yahoo.com","phone": "0804664778","sex" : "Male"},
    {"user": "ope1","pass": "opepass","email": "ope@gmail.com","phone": "0903322778","sex" : "Male"}
]}

p=a["Details"]
x=l[1]
y=x["sex"]
print(y)