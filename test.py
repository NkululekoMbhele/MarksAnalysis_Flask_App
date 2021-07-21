import pandas as pd


file1 = open('newNames.txt', 'r')
names = file1.readlines()

file2 = open('newLastNames.txt', 'r')
lastNames = file2.readlines()

file3 = open('studentNumbers.txt', 'r')
studentNumbers = file3.readlines()

file4 = open('classTest1Marks.txt', 'r')
testMarks = file4.readlines()
# initialize list of lists
data = []

for i in range(500): 
    elements = [names[i][:-1], lastNames[i][:-1], studentNumbers[i][:-1], testMarks[i][:-1]]
    data.append(elements)
 
# Create the pandas DataFrame
df = pd.DataFrame(data, columns = ['Name', 'Surname', 'Student Numbers', 'Class Test 1 Marks'])
 
# print dataframe.

#df.to_csv('student_marks.csv', index=False)
df1 = df.copy()

df1.to_excel("output.xlsx")

