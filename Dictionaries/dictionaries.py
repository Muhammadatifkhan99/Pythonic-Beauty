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


d = instructor
#d.clear() #clears out everything from a dictionary
print(d)

#copy---copy a dictionary
#they are unique objects in memory
clone = instructor.copy()

print(clone)

print(clone is instructor) #is checks for the reference in memory

# is checks identity (whether two variables reference the same object in memory).
# == checks equality (whether two objects have the same value).

#FROM KEYS fromkeys()---use to generate default values, its need an iterable collection to be passed into it.

new_user = {}.fromkeys(['name','age','password','bio','website'],'unknown') #set all the values of the list to unknown

print(new_user)
new = {}
new.fromkeys('phone','unknown')
print(new)


#get

print(instructor.get('name'),instructor.get("email")) #if a key is not present we get the None Error



###############################################################////POP##############

print(instructor.pop("owns_dog")) #takes in a key and remove the corresponding value from it, returns the actual value.





#############POP_ITEM#################
#removes a random value from the dictionary
#no key is provided just picks a random number and removes that
print(instructor.popitem())



########update method############

person = {"city" : "ISB"}

print(person)
print(instructor)

person.update(instructor) #the values of the person dictionaries are added to theinstructor dictionaries

print(person) # person is modified
print(instructor) #while instructor will be the same as it is.

person["name"] = "Ali"
print(person)