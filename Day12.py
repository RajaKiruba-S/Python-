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
import shutil

path = "C:\\Users\\Useer\\Desktop\\pythontext.txt"
try:
    os.remove(path)          #delete a file
    os.rmdir(path)           #used to delete only empty directory
    shutil.rmtree(path)      #delete a directory containing files
except FileNotFoundError:
    print("That file was not found.")             
except PermissionError:        #PermissionError:[WinError 5] Access is denied(it won't delete empty folder)
    print("You do not have permisiion to delete that.")
except OSError:
    print("You can't delete that(empty folder) using that(os.rmdir(path)) function.")
else:
    print(path+" was deleted.")

##Module  (>>a file containing python code. May contain functions, classes, etc.
#          >>used with modular programming, which is to seperate a program into parts)

import modulemessages          #we are importing the main module 

modulemessages.hello()
modulemessages.bye()

import modulemessages as msg

msg.hello()
msg.bye()

from modulemessages import hello,bye

hello()
bye()

# all the above 3 type of code will give same o/p
#Hello, Have a great day!
#Bye, Have a wonderful time!

help("modules")           #it will give all the available modules in python


