#a data structure that consist of key value pairs
#keys are use to describe data and the values represent them

instructor = {
    "name" : "Atif",
    "owns_dog": True,
    "num_courses": 4,
    "favourite_lang": "C++",
    "is_hilarious" : False,
    73: "fav_number"
}

#dic function
#pass key values pairs to the dict function and this will automatically convert it into a dictionary

dictsion  = dict(key = "value",age = 10.5)
print(dictsion)

#getting a value out of the dictionary is to pass in a key
dictsion["key"]
# dictsion["nothing"] #return keyError

#Accessing all values in a dictionary
for value in instructor.values():
    print(value)

#Accessing all keys in a dictionary
for value in instructor.keys():
    print(value)


#for both accessing the keys and values out of dictionary
for k,v in instructor.items():
    print(f"key is {k} and value is {v}")


#no order is guaranteed in dictionaries, but promised in list

#checking for existance of certain key in dictionary
#this only check the keys
if "n" in instructor:
    print("all is well")
else: 
    print(False)