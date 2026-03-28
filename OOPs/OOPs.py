class User:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age

s1 = User("Atif","Khan",20)
print(s1.first,s1.last,s1.age)
s2 = User("Ali","Khan",20)
print(s2.first,s2.last,s2.age)