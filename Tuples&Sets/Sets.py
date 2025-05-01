#SETS
#collections of data that do not have duplicate values
#elements are not ordered
#numbers, strings etc
#no order so cannot access elements by index



s = {1,2,3}

print(s)

s1 = set({1,2,3,4,5})

print(s1)

print(4 in s1)



cities = ["Mardan","Peshawar","Swat","Buner","Malakand","Mardan","Peshawar","Swat"]

print(set(cities))


citySet = set(cities)

citySet.add("Islamabad")

print(citySet)

citySet.remove("Islamabad")
print(citySet)

#if the argument to be remove is not found in the set, it will throw an error


citySet.discard("Mardan")
citySet.discard("Nothing") #this will not throw an error if city is not found