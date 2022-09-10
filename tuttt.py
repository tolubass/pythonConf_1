x=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<10:
    result="pregnancy"
    if x[i]<=10:
        result="positive"
    elif x[i]<9:
        result="negative"
    elif x[i]<8:
        result="negative"
    elif x[i] < 7:
        result="negative"
    elif x[i]<=0:
        result="negative"
    print ("bimbo is"+ result)
    i+=1
    break
