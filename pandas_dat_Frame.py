import pandas as pd
import numpy as np
exam_data = [{'name': 'Anastasia', 'score': 12.5}, {'name': 'Dima', 'score':9}, {'name': 'katherine', 'score': 16.5}]
df = pd.DataFrame(exam_data)
for index, row in df.iterrows():
    print(row['name'], row['score'])