#functions allows us to organize things

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