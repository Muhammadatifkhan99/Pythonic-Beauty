#a data structure that consist of key value pairs
#keys are use to describe data and the values represent them
from functools import total_ordering

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
print("dict items in dictionaries")
print(instructor.values())
print(instructor.keys())
print(instructor.items())


for value in instructor.values():
    print(value)

#Accessing all keys in a dictionary
for k in instructor.keys():
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
#pop takes in the key of the dictionary and removes the corresponding value from it, returns the actual value.

print(instructor.pop("owns_dog")) #takes in a key and remove the corresponding value from it, returns the actual value.

d22 = {"name":"ali"}
# print(d22.popitem()) #no item specified so a random one will be removed
print(d22.pop("name"))



#############POP_ITEM#################
#removes a random value from the dictionary
#no key is provided just picks a random number and removes that
print(instructor.popitem())
#updateitem removes a random key value pair from the dictionary





########update method############

person = {"city" : "ISB"}

print(person)
print(instructor)

person.update(instructor) #the values of the person dictionaries are added to the instructor dictionaries
#the person dictionary is updated with the instructor values.


print(person) # person is modified
print(instructor) #while instructor will be the same as it is.

person["name"] = "Ali"
print(person)


#modelling a spotify playlist

playlist = {
    "title": "summer vibes",
    "author": "atif khan",
    "songs": [
        {"title": "song1", "artist": ["artist1"], "duration": 2.5},
        {"title": "song2", "artist": ["artist2"], "duration": 3.0},
        {"title": "song3", "artist": ["artist3"], "duration": 2.0}
    ]
}
total_duration = 0
for song in playlist["songs"]:
    total_duration = total_duration + song["duration"]
print(total_duration)




#Dictionary Comprehensions
print("Dictionary Comprehsions")

nums = dict(first = 1, second = 2, third = 3)

squared_nums = {key: value ** 2 for key, value in nums.items()}
print(squared_nums)

print({num: num**2 for num in [1,2,3,4,5]}) #this is making a new dictionary but starting with a list

instructor = {
    "name" : "atif",
    "city": "san francisco",
    "color": "purple"
}
print(instructor)

print({k.upper(): v.upper() for k,v in instructor.items()})

nums_list = [1,2,3,4,5,6,7,8]

print({num:("even" if num % 2 == 0 else "odd") for num in nums_list})

# print({num:("even" if num % 2 == 0 else "odd") for num in range(1,100)})




#EXCERCISES

#1.
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]
answer  = {list1[i]:list2[i] for i in range(0,len(list2))}
print(answer)

#2.
person =  [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
things0 = {k:v for k,v in person}
things = dict(person)
print(things0)
print(things)

print({p[0]:p[1] for p in person})

#3.
ascii = {i:chr(i) for i in range(65,91)}
print(ascii)





