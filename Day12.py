##copyfile() = copies contenet of a file
# copy() = copyfile+permission mode+destination can be directory
# copy2() = copy()+copies metadata(file's creation and modification times)

import shutil
shutil.copyfile("C:\\Users\\Useer\\Desktop\\pythontext.txt","C:\\Users\\Useer\\Desktop\\copytext.txt")   #str,dst

##Move a file

import os

source ="C:\\Users\\Useer\\Desktop\\pythontext"
destination ="C:\\Users\\Useer\\Desktop\\movingfile"

try:
    if os.path.exists(destination):
        print("There is already a file there.")
    else:
        os.replace(source,destination)
        print(source+" was moved.")
except FileNotFoundError:
    print(source+" was not found.")

##delete a file

import os

path = "C:\\Users\\Useer\\Desktop\\pythontext.txt"
try:
    os.remove(path)
except FileNotFoundError:
    print("That file was not found")             #PermissionError: [WinError 5] Access is denied(it won't delete empty folder)
except PermissionError:
    print("You do not have permisiion to delete that.")
else:
    print(path+" was deleted.")
