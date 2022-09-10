import matplotlib.pyplot as py
import numpy as np
arr = np.array([10,15,20,60,70,90,130,135,137,240])
label = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct"]
py.pie(arr, labels=label)
py.show()

