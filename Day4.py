#String Slicing

name="Raja Kiruba"
first_name=name[0:4]           #(we can't use[0:3]bcs of exclusive)
                               #name[:4]also crct
last_name=name[5:11]           #name[5:]also crct

print(first_name)              #Raja
print(last_name)               #Kiruba

funky_name=name[0:11:3]        #[::3]also crct
print(funky_name)              #Raib

reversed_name=name[::-1]       #[0:end:-1]
print(reversed_name)           #aburiK ajaR

#slice() used to create a slice function
website1="http://google.com"
website2="http://wikipedia.com"

slice=slice(7,-4)             #here we are using neg index to denote ending

print(website1[slice])        #google
print(website2[slice])        #wikipedia

#If statement (a block of code that will execute if the condition is true)

mark=int(input("What is your mark?"))        #What is your mark?--
if mark>=45:
    print("You are pass.")                   #50 You are pass.
elif mark<0:
    print("bad:( study well")                #-1 bad:( study well
elif mark==100:
    print("You got full mark!!")             #100 You are pass.(the order of the is statements does matter)
else:
    print("You are fail.")                   #0 You are fail.
