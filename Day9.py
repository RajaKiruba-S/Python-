##Variable Scope       (>>The region that a varaible is recoganized
#                       >>A variable is only available from inside the region it is created.
#                       >>A global and local scoped variables can be created.)

name="kir"                    #glopal variable(available inside&outside fn)
def display_name():
    name="Raj"                #local variable(available inside fn)
    print(name)
display_name()        #Raj    #function call(to print local scope)
print(name)           #kir    #to print glopal scope


name="kir"
def display_name():
    name="Raj"
display_name()        #Kir     #there is no local variable, so it uses the global variable
print(name)           #kir

##*args parameters:       (>>it will pack all the arguments into a tuple
#                          >>function can accepy varying amount of args)
def add(num1,num2):
    sum = num1+num2
    return sum
print(add(1,2,3))           #TypeError: add() takes 2 positional arguments but 3 were given

##to solve this we use *arguments

def add(*addition):
    sum = 0
    for i in addition:
        sum += i
    return sum
print(add(1,2,3))            #6
print(add(1,2,3,4))          #10

##if we want to change or assign the value in arguments,
#it is not possible in tuble so we have to change to list
def add(*addition):
    sum=0
    #addition[0]=0           #error (tuple cant assign value)
    addition=list(addition)
    addition[0]=0
    for i in addition:
        sum+=i
    return sum
print(add(1,2,3))            #5
print(add(1,2,3,4))          #9

##**kwargs              (>>it will pack all the arguments into dictionary
#                        >>a function can accept varying amount of keyword argumments)

#def hello(first,last):
#    print("Hello "+first+" "+last)
#hello(first="Bro",mid="Code",last="Dude")            #TypeError: hello() got an unexpected keyword argument 'mid'
#                                                     2 parameters, 3 arguments

def hello(**names):
    print("Hello "+names['first']+" "+names['last'])
hello(first="Bro",mid="Code",last="Dude")              #Hello Bro Dude

#if we wan5t to print whole name
def hello(**names):
    print("Hello ",end=" ")
    for key,value in names.items():
        print(value,end=" ")
hello(first="Bro",mid="Code",last="Dude")              #Hello  Bro Code Dude
hello(tittle="Mr.",first="Bro",mid="Code",last="Dude") #Hello  Mr. Bro Code Dude
