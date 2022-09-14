print("Weight_detector")
print("Drum_tanker = 200kg")
p = int(input("Enter weight inside the drum tank:"))
j=200-(p)
h=0
for h in range (5,31):
    if p>=200:
        print("tank is already full")
        break
    elif p>=5 and p<=30:
        print(str(j) + str("kg is still needed to fill the tank"))
        break
    else:
        print("incorrect weight value")
        break

t=int(input("Enter weight inside the drum tank:"))
q=p-t
print(str(q) + str("kg is still needed to fill the tank"))
if t >= 200:
    print("tank is already full")
elif t >= 5 and t <= 30:
    print(str(t) + str("kg is still needed to fill the tank"))
