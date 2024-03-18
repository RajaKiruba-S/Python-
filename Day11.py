##Exception Handling  (events detecting during execution that interupt the flow of a program)

numerator = int(input("Enter a number to divide:"))
dinominator = int(input("Enter a number to divide by:"))
result = numerator/dinominator
print(result)

#This will generate error. To handle this exception we can use exception handling.

try:
    numerator = int(input("Enter a number to divide:"))
    dinominator = int(input("Enter a number to divide by:"))
    result = numerator/dinominator
    #print(result)
except ZeroDivisionError:
    print("You can't divide by zero.")
except ValueError:
    print("Enter only number plz.")
except Exception:
    print("Something went wrong.")
else:
    print(result)
finally:
    print("This will always execute.")



#Enter a number to divide:5
#Enter a number to divide by:0
#You can't divide by zero.
#This will always execute.

#Enter a number to divide:5
#Enter a number to divide by:pizza
#Enter only number plz.
#This will always execute.

#Enter a number to divide:5
#Enter a number to divide by:2
#2.5
#2.5
#This will always execute.

##File Detection:

import os
path = "C:\\Users\\Useer\\Desktop\\pythontext.txt"
if os.path.exists(path):
    print("The file exists.")
    if os.path.isfile(path):
        print("This is a file.")
    elif os.path.isdirect(path):
        print("This is a directory.")
else:
    print("The file dosen't exist.")

#here we created a file.
#The file exists.
#This is a file.

##reading a file

with open("C:\\Users\\Useer\\Desktop\\pythontext.txt") as file:
    print(file.read())

print(file.closed)

#Hi, This is Kiruba
#True

##writing a file
text = "heyyyy\nwhat's up?\nwhat's going on??"
with open("C:\\Users\\Useer\\Desktop\\pythontext.txt",'w') as file:
    print(file.write(text))

#Now the text will be written in the file.
