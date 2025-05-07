def square(num): return num * num
print(square(2))

lambda num: num * num
#lambas are functions that have no names.
#smiliar to anonymous functions in JS

square2 = lambda num: num * num * num

print(square2(1))



##MAPs
# a standard function that accept at least two arguments a function and an iterable



##FILTERS
# there is a lambda for each value in the iterable

l = [1,2,3,4,5,6]

evens = list(filter(lambda x: x % 2 == 0,l))

print(evens)


names = ["lassie","colt", "rusty"]

instructor = list(map(lambda name: f"Your Instructor is {name}", filter(lambda value: len(value) < 5, names)))
print(instructor)

# exact_name =[name for name in names: if len(name) < 5]


#ANY AND ALL;;;;;;;;;;;;;;;
#return true if all the elements of the iterable are truthy

yes = all([char for char in "aeio" if char in "aeiou"])
print(yes)

#ANY
#return true if any iterable of the collection is truthy

#SORTED 
#sort the data in ascending order by default, but does not modify the original list,tuple instead returna new one....
nums = [1,2,3,4,1,2,3,1,3,2,4,2,4,9,7,6,4,5,6,2,2]

print(sorted(nums))

print(nums)


#how to sort a list of dictionaries, for that we have supply an extra argument called key to the sort functoins

