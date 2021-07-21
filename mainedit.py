import random


def names():
    fileNames = open('./TextFiles/names.txt', 'r')
    Lines = fileNames.readlines()


    newLines = []

    for i in range(500):
        newLines.append(str(Lines[i].capitalize()).strip() + '\n')

    file1 = open('newNames.txt', 'w')
    file1.writelines(newLines)
    file1.close()
    
def lastNames():
    fileNames = open('./TextFiles/lastNames.txt', 'r')
    Lines = fileNames.readlines()
    newLines = []

    for i in range(500):
        newLines.append(str(Lines[i].capitalize()).strip() + '\n')

    file1 = open('newLastNames.txt', 'w')
    file1.writelines(newLines)
    file1.close()
    
def makeStudentNumbers():
    fileNames = open('newNames.txt', 'r')
    FirstLines = fileNames.readlines()
    
    fileLastNames = open('newLastNames.txt', 'r')
    LastLines = fileLastNames.readlines()
    
    studentNumbers = []
    
    for i in range(500):
        x = str(i)
        sec1 = str(FirstLines[i][:3]).upper().strip()
        sec2 = str(LastLines[i][:3]).upper().strip()
        sec3 = '{0}'.format(x.zfill(3))
        uniqueNumber = sec1 + sec2 + sec3 + '\n'
        studentNumbers.append(uniqueNumber)
    
    file2 = open('studentNumbers.txt', 'w')
    file2.writelines(studentNumbers)
    file2.close()
    
def randomNumbersTestOne():
    randomlist = []
    
    for i in range(0, 500):
        n = random.randint(15, 99)
        randomlist.append(n)
        
    newRandomList = []
    
    for l in randomlist:
        x = str(l) + '\n'
        newRandomList.append(x)
    
    file3 = open('classTest1Marks.txt', 'w')
    file3.writelines(newRandomList)
    file3.close()
    
def spliceThem(): 
    filename = ['newNames.txt', 'newLastNames.txt', 'studentNumbers.txt', 'classTest1marks.txt']
    newFilename = ['newNames1.txt', 'newLastNames1.txt', 'studentNumbers1.txt', 'classTest1marks1.txt']
    
    data = []
    for i in range(4):        
        fileLastNames = open(filename[i], 'r')
        fileLines = fileLastNames.readlines()
        
        for j in range(500):
            data.append(fileLines[j]) 
        
        file2 = open(filename[i], 'w')
        file2.writelines(data)
        file2.close()
        data = []


names()
lastNames()
makeStudentNumbers()      
#randomNumbersTestOne()        
#spliceThem()