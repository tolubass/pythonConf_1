print("Weight_detector")
print("Drum_tanker = 200kg" )
w1=5
w2=30
w3=20
w4=28
w5=16
w6=10
w7=18
w8=26
w9=23
w10=24

total_weight=200
x=(w1+w2+w3+w4+w5+w6+w7+w8+w9+w10)

h=int(input("Enter weight inside the drum tank:"))
while h >= 200:
    print(h)
    if h == 200:
        print("full tank.")
    break
p=200-(h)
if h>200:
    print("tank is overfull")
elif h==w1:
    print(str(p) + str("kg is still needed to fill the tank"))
elif h==w2:
    print(str(p) + str("kg is still needed to fill the tank"))
elif h==w3:
    print(str(p) + str("kg is still needed to fill the tank"))
elif h==w4:
    print(str(p) + str("kg is still needed to fill the tank"))
elif h==w5:
    print(str(p) + str("kg is still needed to fill the tank"))
elif h==w6:
    print(str(p) + str("kg is still needed to fill the tank"))
elif h==w7:
    print(str(p) + str("kg is still needed to fill the tank"))
elif h==w8:
    print(str(p) + str("kg is still needed to fill the tank"))
elif h==w9:
    print(str(p) + str("kg is still needed to fill the tank"))
elif h==w10:
    print(str(p) + str("kg is still needed to fill the tank"))
else:
    print("unrecognized weight(kg)")
D=int(input("Enter weight inside the drum tank:"))
q=p-D
print(str(q) + str("kg is still needed to fill the tank"))
R=int(input("Enter weight inside the drum tank:"))
g=q-R
print(str(g) + str("kg is still needed to fill the tank"))
u=int(input("Enter weight inside the drum tank:"))
c=g-u
print(str(c) + str("kg is still needed to fill the tank"))
n=int(input("Enter weight inside the drum tank:"))
t=c-n
print(str(t) + str("kg is still needed to fill the tank"))
a1=int(input("Enter weight inside the drum tank:"))
a2=t-a1
print(str(a2) + str("kg is still needed to fill the tank"))
a3=int(input("Enter weight inside the drum tank:"))
a4=a2-a3
print(str(a4) + str("kg is still needed to fill the tank"))
a5=int(input("Enter weight inside the drum tank:"))
a6=a4-a5
print(str(a6) + str("kg is still needed to fill the tank"))
y1= (int(q+g+c+t+a2+a4+a6))
print(y1)
