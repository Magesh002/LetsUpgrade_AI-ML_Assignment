import pandas as pd
import numpy as np

exam_data = {
    'name': ['Magesh', 'Karthi', 'Ramana', 'Kowshik', 'Saravana', 'Thamizh', 'Kishore', 'Sparky', 'Mohan'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2],
    'qualify': ['yes', 'no', np.nan, 'no', np.nan, 'yes', 'yes', 'no', 'no']}
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

df = pd.DataFrame(exam_data, index=labels)
print(df)
# print(type(df))
print("\nPrinting the name and score columns:\n", df[['name', 'score']])

exam_data2 = {
    'name': ['Ram', 'Ashok', 'Alraiyan'],
    'score': [11.5, 6, np.nan],
    'attempts': [2, 3, 2],
    'qualify': ['yes', np.nan, 'no']}

df1 = pd.DataFrame(exam_data)
df2 = pd.DataFrame(exam_data2)
df3 = pd.concat([df1, df2])
print("\nConcatenate 2 dataFrame objects:\n", df3)

print("\nMissing Data:\n", df3.isna())

print("\nArray of data in list:\n", pd.Series([3, 13, 2, 4, 22, 5, 43]))