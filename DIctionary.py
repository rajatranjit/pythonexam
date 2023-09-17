
my_dict = {
    "Name":"kamal",
    "Age":22,
    "Address":"Kathmandu"
}
my_dict["Age"]=16  # age correction
my_dict["phone"]=9849027435

print(my_dict)
print(len(my_dict))

keys1 = my_dict.keys()
print(keys1)
value = my_dict.values()

del my_dict["Age"]
print(my_dict)

a = my_dict.pop("Age")
print(my_dict)
print(a)

del my_dict[1]
print(my_dict)



my_dict = {
    "Name":"kamal",
    "Age":22,
    "Address":{
        "city":"kathmandu",
        "street":"sundhara",
        "zip":{
            "zip1":44600,
            "zip2":44800
        }
    }
}
print(my_dict["Address"]["zip"]["zip2"])  
 


#WAP to find square of every element of list and sum of squares
#WAP to check if a given string is present in list or not
# wap to copy list elements into another list 

