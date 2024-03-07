#Nested loops     (The "inner loop" will finish all of its iterations before finishing one iterations of the "outer loop")

rows = int(input("Enter the rows:"))
columns = int(input("Enter the columns:"))
symbol = input("Eneter the symbol to use:")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")    #here we using end="' to move to next line
    print()                      

#o/p:
#Enter the rows:3
#Enter the columns:3
#Eneter the symbol to use:*
#***
#***
#***

#Loop control statements    (change a loops normal flow)

#break=used to terminate the loop entirely
#continue=skips the next iteration of the loop
#pass=does nothing, acts as a placeholder

while True:
    name=input("Enter your name:")    #Enter your name:
    if  name != "":                   #Enter your name:
        break                         #Enetr your name:kir

phone_number = "123-456-789"
for i in phone_number:         #here we didn't use i in range bcs it is string not int
    if i == "-":
        continue               #-is skiped
    print(i, end="")           #123456789

for i in range(1,21):
    if i == 13:
        pass                   #13 skiped
    else:
        print(i)

#1
#2
#3
#4
#5
#6
#7
#8
#9
#10
#11
#12
#14
#15
#16
#17
#18
#19
#20

#Lists      (used to store multiple items in a single variables)

fruit=["Apple","Orange","Mango","Grapes"]
print(fruit)                      #['Apple', 'Orange', 'Mango', 'Grapes']
for x in fruit:
    print(x)                      #Apple
                                  #Orange
                                  #Mango
                                  #Grapes
print(fruit[0])        #Apple
fruit[0]="Gova"         
print(fruit[0])        #Gova  
fruit.append("Avacado")           #['Gova', 'Orange', 'Mango', 'Grapes', 'Avacado']
fruit.remove("Orange")            #['Gova', 'Mango', 'Grapes', 'Avacado']
fruit.pop()                       #['Gova', 'Mango', 'Grapes']
fruit.insert(0,"pineapple")       #['pineapple', 'Gova', 'Mango', 'Grapes']
fruit.sort()                      #['Gova', 'Grapes', 'Mango', 'pineapple']
fruit.clear()                     #[]#(clear the whole list)
print(fruit)

#2D Lists   (list of lists)

name=["kiruba","prema","kams"]
department=["ECE","CCE"]
section=["A","B"]

college=[name,department,section]
print(college)                         #[['kiruba', 'prema', 'kams'], ['ECE', 'CCE'], ['A', 'B']]

print(college[0][0])                    #kiruba
print(college[2][1])                    #B
print(college[1][2])                    #IndexError: list index out of range
