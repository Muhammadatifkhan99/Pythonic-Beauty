#why we use modules?
#reuse a code, keep your own code dry,
#keep python files small


import random

print(random.choice(["apple", "banana", "cherry", "durian"]))



#importing parts of module using the from key
#we usally wants to import some functions from a particular module


from  random import choice,shuffle,randint

print(random.choice(["apple","banana","cherry","durain"]))
