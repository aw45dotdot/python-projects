dict = {"name":"Muhammad","age":13,"class":"second year"}
print(f'dictionary = {dict}\n')

#no. of items
print(f'No. of items in dictionary is {len(dict)}\n')
print(dict["name"])
print(dict["age"])

list = ["hello","world"]

print(list[0],"\n")
print(dict.keys(),"\n") #print only the keys from a dictionary
print(dict.values(),"\n") #print only the values from a dictionary
print(dict.items(),"\n") #print the key-value pair using () for each item eg. ([('name', 'Muhammad')])

#print the key-value pair using for loop
for key in dict.keys():
    print(key,dict[key],"\n")
    
#check if key exists or not
if "country" in dict:
    print(dict["class"],"\n")
else:
    print("KEY DOESN'T EXIST","\n")
    
print("To change value in dictionary")
dict["age"] = 14
print(dict,"\n")
del(dict["class"])
print(dict,"\n")

#store a list as a value in a dictionary
dict["marks"] = [20,50,75,90]
print(dict,"\n")
print(dict["marks"][2]"\n")
