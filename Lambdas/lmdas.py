def square(num): return num * num
print(square(2))

lambda num: num * num
#lambas are functions that have no names.
#smiliar to anonymous functions in JS
#lambda are one liners functions, it is a nameless function

square2 = lambda num: num * num * num
add = lambda a,b: a+b

print(square2(1))

print(square.__name__)
print(square2.__name__)
print(add.__name__)

##MAPs
# a standard function that accept at least two arguments a function and an iterable
#iterable->something that can be iterated over like a list,tuple,set etc
#runs the lambda function on each element of the iterable and returns a new iterable of the same length containing the results.
nums = [1,2,3,4,5]

doubles = map(lambda x: x * 2, nums)
print(list(doubles))
print(list(doubles))

people = ["Darcy","Christina","Dana","Annable"]

peeps = map(lambda n: n.upper(),people)
print(list(peeps))
print(peeps)



##FILTERS
# there is a lambda for each value in the iterable

l = [1,2,3,4,5,6]

evens = list(filter(lambda x: x % 2 == 0,l))

print(evens)

name = ["austin","penny","anthony","anbgel","billy"]

a_names = filter(lambda n: n[0] == 'a',name)
print(list(a_names))
print(a_names)



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


import sys

list_Comp = sys.getsizeof([x*10 for x in range(1000)])
gen_Exp = sys.getsizeof(x*10 for x in range(1000))

print("List Comprehension size is: ",list_Comp)
print("Generator Expression size is: ",gen_Exp)
#gen expressions are very light weight and very useful and needed.



###SORTED
#it is different from sort, this returns a new sorted list from the items in iterable, like tuple, list etc
print("SORTED")
#it does not modify the original list...
more_numbers = [6,1,8,2]
print(sorted(more_numbers))
print(more_numbers)
#while sort will change the original list, only works with list
nums = [2,3,4,5,6,7]
nums.sort()
print(nums)

#we can specify the direction of sorting by using reverse=True
print(sorted(nums,reverse=True))
#accept a lambda, so we can specify the key based on which we want the arrangements to be
#sorted works with almost any iterable

users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie"]},
    {"username": "katie", "tweets": []},
    {"username": "jeff", "tweets": [],"color":"purple"},
    {"username": "bob123", "tweets": [],"num":10,"color":"teal"},
    {"username": "doggo_luvr", "tweets": ["dogs are the best"]},
    {"username": "guitar_gal", "tweets": []}
]
print(sorted(users,key = lambda user: user["username"]))
print(sorted(users,key=lambda user: len(user["tweets"]),reverse=True))


print("MAX")

print(max(3,67,888))
print(max('a','b','d'))

print(min(1,2,3))
print(min('a','b','d'))


name = ['Arya','Samson','Dora','Tim','Ollivander']
print(min(name))
print(min(n for n in name))
print(min(len(n) for n in name))
print((len(n) for n in name))

print("REVERSED")

nuns = [1,2,3,4]
nuns.reverse()
print(nuns)

for c in reversed("hello world"):
    print(c)


print("LENGTH METHOD")
print(len("ajdfl;akjdlf;jal;dfjal;skdjf;"))

print("ZIP Basics")
#the zip returns an iterator
# returns a list of tuples where the i-th tuple contains the i-th element from each of the argument sequences or iterables.



n1 = [1,2,3,4]
n2 = [4,5,6,7]
s1 = ['haha','baba','dada','fafa']
s2 = ['haha','baba','dada','fafa','kaka']

z = list(zip(n1,n2,s1))
print(z)