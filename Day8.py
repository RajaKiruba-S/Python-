##function    (a block of code which is executed only when it is called)

def hello(name):                #here the name is a parameter
    print("Hello "+name)              
    print("Have a nice day!")         
hello("Kir")                    #here Kir is an argument
hello("Kir")

#Hello Kir
#Have a nice day!
#Hello Kir
#Have a nice day!

def hello(name):                
    print("Hello "+name)              
    print("Have a nice day!")         
my_name="Kir"                    #the parameter can also be written like this
hello(my_name)

def hello(first_name,last_name,age):                
    print("Hello "+first_name+" "+last_name)
    print("You are "+str(age)+"years old")
    print("Have a nice day!")
hello("Raja","Kiruba",19)

#Hello Raja Kiruba
#You are 19years old
#Have a nice day!

##Return statement     (>>functions send python values/objects bach to the caller
#                       >>these values/objects are known as the function's return value)

def mul(num1,num2):
    result=num1*num2
    return(result)
print(mul(6,5))         #we have to use print in arguments bcs the o/p is returned to the caller

x=mul(6,5)              #we can also write like this
print(x)

#30

##keyword arguements    (>>arguments preceded by an identifier when we pass them to a function
#                        >>The order dosen't matter
#                        >>python knows the names of the arguments that our function receives)

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)
hello("Bro","code","Dude")                          #Hello Bro code Dude
hello("Dude","code","Bro")                          #hello Dude code Bro
hello(last="Dude",middle="code",first="Bro")        #Hello Bro code Dude
#we can assign the order of the arguments


##Nested fuction call

num=input("Enter   a positive whole number:")
num=float(num)
num=abs(num)
num=round(num)
print(num)

print(round(abs(float(input("Enter   a positive whole number:")))))

#Enter   a positive whole number:-3.14
#3
