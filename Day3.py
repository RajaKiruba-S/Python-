#user inputs

name=input("Who are you?")            #Who are you?kir
print("Hello "+name)                  #Hello kir

#mark=input("What is your mark?")      #What is your mark?95
#mark=mark+1                           #TypeError: can only concatenate str (not "int") to str

mark=int(input("What is your mark?"))
mark=mark+1
#print("You got "+mark+"marks.")        #TypeError: can only concatenate str (not "int") to str
                                        #we can't add sting to integer("You got "+mark+"marks.")
print("You got "+str(mark)+" marks.")   #You got 96 marks.

percentage=float(input("What is your percentage?"))      #What is your percentage?89.5
print("Your % of mark is "+str(percentage))              #Your % of mark is 89.5

