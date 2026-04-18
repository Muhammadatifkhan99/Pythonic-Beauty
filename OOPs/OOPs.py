# class User:
#     def __init__(self,first,last,age):
#         self.first = first
#         self.last = last
#         self.age = age
#
# s1 = User("Atif","Khan",20)
# print(s1.first,s1.last,s1.age)
# s2 = User("Ali","Khan",20)
# print(s2.first,s2.last,s2.age)


# name mangling: when we put two underscore before the name of a method or an attribute
#name mangling make the variable particular to the class it was from. so to access it we need to use the class name.
#name mangling make the attributes or methods particular to that class so if you want to access it you have to use the name of class

# _name    -> pure convention to declare something private
# __name   -> name mangling
# __name__ -> dunder methods

class Person:
    active_users = 0
    def __init__(self):
        self.name = "Atif"
        self._age = 15 #python way of defing private variable, it can be accessed outside the class not restriction but just a notation
        self.__msg = "Hello"
        self.__lol = "HAHAHAHA"
        Person.active_users = +1

p = Person()

print(p.name)
print(p._age)
print(dir(p))
print(p._Person__lol)
print(p._Person__msg)


# class Attributes
# we can define a class attributes directly on a class that are shared by all the instances of a class
# and the class itself
print(Person.active_users)