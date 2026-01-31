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

