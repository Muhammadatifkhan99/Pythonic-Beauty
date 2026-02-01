#functions allows us to organize things
#think of functions as a set of instructions that can be reused
#think of functions as a block of code that can be called multiple times
#think of functions as a bunch of lines of code wrapped up into a nice little package.

# def name_of_function():
#     print("Hello")

# name_of_function()

from random import random

# random() gives a number between zero and one but does not include 1



def print_square_7():
    print(7*7)

print_square_7()


def flip_coin():
    if random() > 0.5:
        return "HEAD"
    else:
        return "TAILS"
    
print(flip_coin())

#this will override the above function
def flip_coin():
    if random() > 0.5:
        return "Head"
    else:
        return "Tails"
    

def exponent(num,power=2):
    return num ** power

print(exponent(2,3))
print(exponent(2,3))
print(exponent(4,4))

#default parameters always needs to be in the end of the function definition otherwise it will confuse python


#parameters
print("Functions Parameters")
def square(k):
    return k*k;

print(square(2))


print("Functions Parameters Ends")



#KEYWORD ARGUMENTS-----useful if you know the names of the parameters
print("Keyword Arguments")


def full_name(first,last):
    return f"Your name is {first} {last}"

print(full_name(first="Atif",last="Khan"))


squaure = exponent(power=2,num=10)
print(squaure)


#SCOPE--WHERE OUR VARIABLES ARE ACCESSIBLE IN THE PROGRAM

# total = 0

# def increment():
#     total = total +  1
#     return total

# increment()


# total = 0

# def increment():
#     global total
#     total = total + 1
#     return total

# increment()


#DOC STRING

def say_hello():
    """this function will print helloworld to the consol"""
    print("hello")

print(say_hello.__doc__)


#Excercises

#3.

def last_element(l):
    return l[len(l)-1]

print(last_element([1,2,3,4,5,6,7,8]))


#4.

def greater_num(a,b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    else:
        return "Both are equal"

print(greater_num(5,2))


def single_letter_count(str1,str2):
    count = 0
    for s in str1:
        if s == str2:
            count += 1
    if count > 0:
        return count
    else:
        return None

print(single_letter_count("hello","l"))


#4.count of letters as a dictionary

def letter_count(s):
    return {l:s.count(l) for l in s}

print(letter_count("hello"))


#5. is_palindrome function

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("welcome"))

#6. search times

def search_times(lst, target):
    count = 0
    for l in lst:
        if l == target:
            count += 1
    return count
print(search_times([1,2,3,4,3,3,7,8,9],3))

def even_mul_list(l):
    product = 1
    for i in l:
        if i % 2 == 0:
            product *= i
    return product

print(even_mul_list([1,2,3,4,5]))


#7. capitalize the first letter

def capitalize(s):
    return s[0].upper() + s[1:]
print(capitalize("hello"))



def for_truthy_values(l):
    lst = []
    for i in l:
        if i == True:
            lst.append(i)
    return lst

print(for_truthy_values([True,False,None,0,1]))


#8. intersection

def intersection(l1,l2):
    l3 = []
    for i in l1:
        if i in l2:
            l3.append(i)
    return l3

print(intersection([1,2,3,4,5,6,7],[3,4,5,6,7]))

