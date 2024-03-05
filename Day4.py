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
