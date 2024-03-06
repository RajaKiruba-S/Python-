##Logical operators  ((and,or,not)=used to check if two are more conditional statement is true)

temp=int(input("What is the temperature?"))
if temp >= 0 and temp <= 30:                    #What is the temperature?50
    print("The temperature is good today!")     #The temperature  is bad today
    print("Go outside")                         #Go outside
    
elif temp < 0 or temp >30:                      #What is the temperature?-10
    print("The temperature  is bad today")      #The temperature  is bad today
    print("Stay inside")                        #Stay inside

if not(temp >= 0 and temp <= 30):               #What is the temperature?-10
    print("The temperature  is bad today")      #The temperature  is bad today
    print("Stay inside")                        #Stay inside
    
elif not(temp < 0 or temp >30):                 #What is the temperature?50
    print("The temperature is good today!")     #The temperature  is bad today
    print("Go outside")                         #Go outside

##While loop    (a stmt execute a block of code as long as its cond remains true)

mark = ""
while len(mark) == 0:
    mark = input("Enter your mark:")
                                      #Enter your mark:
print("you got "+ mark +" marks")     #Enter your mark:
                                      #Enter your mark:95
                                      #you got 95 marks

#anothe way for writing same program

mark = None
while not mark:
    mark = input("Enter your mark:")
                                      #Enter your mark:
print("you got "+ mark +" marks")     #Enter your mark:
                                      #Enter your mark:95
                                      #you got 95 marks

##for loop  (a stmt execute its block of code for a limited times)

for i in range(10):            #Note: all the o/p will print in vertical
    print(i)                   #0,1,....,9
    print(i+1)                 #1,2,3,....,9,10
    
for i in range(50,100):
    print(i)                   #50,51,52,....,99

for i in range(50,100+1,2):
    print(i)                   #50,52,54,....,58,100

#string in loop

for i in "Kiruba Angel":
    print(i)                   #legnA aburiK

#program to print Happy new year using time

import time
for seconds in range(10,0,-1):      #neg index bcs we are countdown in reverse
    print(seconds)                  #10
    time.sleep(1)                   #9
print("Happy New Year!")            #8
                                    #.
                                    #.
                                    #.
                                    #1
                                    #Happy New Year!(the o/p will print with 1 sec sleep)
