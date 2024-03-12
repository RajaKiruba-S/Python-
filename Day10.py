##str.format()                   (>>optional method that gives users
#                                 >>more control when displaying o/p)

animal="cow"
item="moon"
print("The "+animal+" jumped over the "+item)                                 #The cow jumped over the moon
print("The {} jumped over the {}".format(animal,item))                        #The cow jumped over the moon
print("The {1} jumped over the {0}".format(item,animal))                      #The cow jumped over the moon
print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #The cow jumped over the moon
text="The {} jumped over the {}"
print(text.format(animal,item))                                               #The cow jumped over the moon

name="Bro"
print("Hello, my name is {}".format(name))                                    #Hello, my name is Bro
print("Hello, my name is {:10}.Nice to meet you".format(name))                #Hello, my name is Bro       .Nice to meet you
print("Hello, my name is {:<10}.Nice to meet you".format(name))               #Hello, my name is Bro       .Nice to meet you
print("Hello, my name is {:>10}.Nice to meet you".format(name))               #Hello, my name is        Bro.Nice to meet you
print("Hello, my name is {:^10}.Nice to meet you".format(name))               #Hello, my name is    Bro    .Nice to meet you

number=3.14679
print("The number pi is {:.2f}".format(number))                               #The number pi is 3.15
                
num=1000
print("The number is {:,}".format(num))                                       #The number is 1,000
print("The number is {:b}".format(num))                                       #The number is 1111101000
print("The number is {:o}".format(num))                                       #The number is 1750
print("The number is {:x}".format(num))                                       #The number is 3e8
print("The number is {:X}".format(num))                                       #The number is 3E8
print("The number is {:e}".format(num))                                       #The number is 1.000000e+03
print("The number is {:E}".format(num))                                       #The number is 1.000000E+03

##Random numbers

import random
x=random.randint(1,6)
y=random.random()
list=['rock','paper','scissors']
z=random.choice(list)
cards=[1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
random.shuffle(cards)

print(x)                  #5
print(y)                  #0.29401117135807264
print(z)                  #rock
print(cards)              #[8, 9, 'Q', 2, 'K', 'A', 5, 'J', 4, 1, 3, 7, 6]

#it rendomly gives the output
