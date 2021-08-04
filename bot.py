import pandas as pd
import matplotlib.pyplot as pl

df = pd.read_csv (r'./uploads/student_marks.csv')

# columns
cols = df.columns.values
print(cols)

# Number of rows and columns
print(df.shape[0])
print(df.shape[1])

# mean 
print(df[cols[-1]].mean())

# median
print(df[cols[-1]].median())

# lowest mark 
print(df[cols[-1]].min())

# highest mark
print(df[cols[-1]].max())

df1 = df[(df.filter(like=cols[-1]) >= 50).any(axis=1)]
df2 = df[(df.filter(like=cols[-1]) < 50).any(axis=1)]

print("how many students got greater than 50")
print(df1.shape[0])
print("how many students got less than 50")
print(df2.shape[0])

data = {'C':20, 'C++':15, 'Java':30,
        'Python':35}

courses = list(data.keys())
values = list(data.values())

pl.bar(courses, values, color ='maroon',width = 0.4)
pl.show()