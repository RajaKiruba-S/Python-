#variables
#string
name="Kiruba"            #kiruba
print(name)
print(type(name))        #<class 'str'>
print("name")            #name

name1="Raja"
name2="Kiruba"
fullname=name1+name2
print(fullname)           #RajaKiruba

fullname=name1+" "+name2
print(fullname)           #Raja Kiruba

print("Hello "+fullname)   #Hello Raja Kiruba


#int...
age=19                    #for integer we don't use ""
print(age)                #19
age+=1
print(age)                #20
print(type(age))          #<class 'int'>

age="20"
print(age)                #20
print(type(age))          #<class 'str'>

print("My age is:"+age)     #TypeError: can only concatenate str (not "int") to str
print("My age is:"+str(age)) #My age is:20


#float...
mark=98.9
print(mark)
print(type(mark))

print("My mark is:"+mark)       #TypeError: can only concatenate str (not "float") to str
print("My mark is:"+str(mark))   #My mark is:98.9


#Boolean...
goodgirl=True                  #for bool we don't use ""
print(goodgirl)                #True
print(type(goodgirl))          #<class 'bool'>

#goodgirl="True"
print(goodgirl)               #True
print(type(goodgirl))         #<class 'str'>

print("Are you a goodgirl?"+goodgirl)        #TypeError: can only concatenate str (not "bool") to str
print("Are you a goodgirl?"+str(goodgirl))   #Are you a goodgirl?True
