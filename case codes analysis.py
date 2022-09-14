import matplotlib.pyplot as py
import pandas as pd
import numpy as np
df = pd.read_csv("http://localhost/proj/cases.csv")
print(df)
print("\n sum total of the CRIMINAL DAMAGE")
print(df.iloc[[6]])
s = {"CRIMINAL DAMAGE":[6.45,11.3,13.0,16.13,11.3,6.45,0,13.0,0,4.8,13.0,4.8],
     "initial value": [4,7,8,10,7,4,0,8,0,3,8,3],
     "MONTHS": ["April","August", "December", "February", "January", "July", "June", "March", "May", "November", "October","September"]}
f = pd.DataFrame(s)
print(f)

print("\n print initial value of CRIMINAL DAMAGES ROW:")
print(f["initial value"].sum())

x = s["MONTHS"]
y = s["CRIMINAL DAMAGE"]
py.plot(x,y, color= "green",)
py.xlabel("months")
py.ylabel("rate in %")
py.title("CRIMINAL DAMAGES RECORDED IN THE COUNTRY ")
py.show()
