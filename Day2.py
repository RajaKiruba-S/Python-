#string methods

name="Kiruba Angel"
print(name)

print(len(name))            #12
print(name.find("i"))       #1(return the index)
print(name.capitalize())    #Kiruba angel(capitalize the 1st letter only)
print(name.upper())         #KIRUBA ANGEL
print(name.lower())         #kiruba angel
print(name.isdigit())       #False

name1=123                     
#print(name1.isdigit())        #AttributeError: 'int' object has no attribute 'isdigit'
name2="123"
print(name2.isdigit())       #True

name3="KirubaAngel"
print(name3.isalpha())       #True

print(name.count("u"))       #1(return the count of the given letter)
print(name.replace("a","s")) #Kirubs Angel
print(name*3)                #Kiruba AngelKiruba AngelKiruba Angel
print(name3*3)               #KirubaAngelKirubaAngelKirubaAngel

