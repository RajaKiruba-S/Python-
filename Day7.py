##tuble    (collection which is ordered and unchangeable used to group togrther related data)

student=("kiruba",19,"female")

print(student.count("kiruba"))                  #1
print(student.count("Bro"))                     #0

print(student.index("female"))                  #2

for x in student:
    print(x)                                    #kiruba
                                                #19
                                                #female
if "kiruba" in student:
    print("kiruba is here")                     #kiruba is here

##Set   (collection which is unordered unindexed. #No duplicate values)
#        in tuble o/p will come in any order

fruit={"apple","orange","grapes"}
for x in fruit:                 #apple
    print(x)                    #grapes
                                #orange               
    
                                #apple
fruit.add("mango")              #mango
                                #orange
                                #grapes

fruit.remove("grapes")          #mango
                                #apple
                                #orange

food={"dosa","idly","rice"}
fruit.update(food)               #idly   #[food.update(fruit)
                                 #rice    for x in food:
for x in fruit:                  #apple       print(x)]
    print(x)                     #dosa
                                 #mango
                                 #orange

dinner_table=fruit.union(food)
print(dinner_table)               #{'rice', 'orange', 'grapes', 'dosa', 'apple', 'idly'}

fruit={"apple","orange","grapes"}
food={"dosa","idly","rice","grapes"}
print(fruit.difference(food))     #{'apple', 'orange'}
print(food.difference(fruit))     #{'dosa', 'idly', 'rice'}
print(fruit.intersection(food))   #{'grapes'}

##Dictionary      (>>a changable, unordered collection of unique key:vale pairs)
#                 >>Fast bcs they use hashing, allow us to access a value quickly
#                 >>mutable(thwy change them after the program is already running))


capitals={'USA':'Washington DC',
          'India':'New Delhi',
          'China':'Beijing',
          'Russia':'Moscow'}
print(capitals)                #{'USA': 'Washington DC', 'India': 'New Delhi', 'China': 'Beijing', 'Russia': 'Moscow'}
print(capitals['Russia'])      #Moscow
#print(capitals['Germany'])     #KeyError: 'Germany'
print(capitals.get('Germany')) #None
print(capitals.keys())         #dict_keys(['USA', 'India', 'China', 'Russia'])
print(capitals.values())       #dict_values(['Washington DC', 'New Delhi', 'Beijing', 'Moscow'])
print(capitals.items())        #dict_items([('USA', 'Washington DC'), ('India', 'New Delhi'), ('China', 'Beijing'), ('Russia', 'Moscow')])

for key,value in capitals.items():
    print(key,value)           #USA Washington DC
                               #India New Delhi
                               #China Beijing
                               #Russia Moscow

capitals.update({'Germany':'Berlin'})  #{'USA': 'Washington DC', 'India': 'New Delhi', 'China': 'Beijing', 'Russia': 'Moscow', 'Germany': 'Berlin'}
capitals.update({'USA':'Los Vegas'})   #{'USA': 'Los Vegas', 'India': 'New Delhi', 'China': 'Beijing', 'Russia': 'Moscow', 'Germany': 'Berlin'}
capitals.pop('China')                  #{'USA': 'Los Vegas', 'India': 'New Delhi', 'Russia': 'Moscow', 'Germany': 'Berlin'}
capitals.clear()                       #{}
print(capitals)
