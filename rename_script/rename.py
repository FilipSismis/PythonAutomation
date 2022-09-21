import os

fileList = os.listdir('.//')
fileList.remove('rename.py')
for file in fileList:
    print('Checking if ' + file + ' is file or dir')
    eof = os.path.splitext(file)[1]
    if not eof:
        fileList.remove(file)
        print(file + ' was removed from the list')

for file in fileList:
    if(file.endswith(".txt")):
        fileList.remove(file)

increment = 1
filesToBeRemoved = []
alreadyRenamed = False

for file in fileList:
    oldName = os.path.splitext(file)[0]
    print(oldName)
    try:
        numberName = int(oldName)
        if(numberName < 400 and numberName >= increment):
            increment = numberName
            alreadyRenamed = True;
            filesToBeRemoved.append(file)
    except ValueError:
        print("Not a number name")

for file in filesToBeRemoved:
    fileList.remove(file)
    print("removed from list: " + file)

if(alreadyRenamed): increment += 1
    
for file in fileList:
    extension = os.path.splitext(file)[1]
    newName = str(increment) + extension
    os.rename(file, newName)
    print('File '+ file + ' was renamed to number:' + str(increment))
    increment += 1
