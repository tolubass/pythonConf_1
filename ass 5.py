x= [2, 5, 7, 4, 3, 1, 0, 5, 9, 8]
y= [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
total=len(x)
a=0
grandtotal=0
while a<total:
    c=x[a]+y[a]
    grandtotal=(grandtotal+c)
print(grandtotal)
a+=1
print("grandtotal="+str(grandtotal))
