# *args or star args--special operator that we can pass into our functions as a parameters
# this gather all remaining arguments as tuple

#to get out all the values out of the args, need to iterate over the args, its a tuple
def sum_of_all_nums(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(sum_of_all_nums(2,3,4,5,3,5,4,3,2,2,4))



##KWARGS



#a special operator we can pass to functions
#gather remaining keyword arguments as a dictionary, and store it in a dictionary instead of a tuple


def fav_color(**kwargs):
    print(kwargs)

fav_color(colt="red",ruby="purple",ethel="black")


#LOOPING THRU KWARGS
print("Looping through kwargs".upper())
def fav_color(**people):
    for name,color in people.items():
        print(f"{name}'s lovely color is {color}")

fav_color(colt="red",ruby="purple",ethel="black")

#PARAMETER ORDERING

#THE FOLLOWING ORDER SHOULD BE FOLLOWED BY PARAMETERS PASSED INTO FUNCTIONS
# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs

#ARGUMENTS UNPACKING-----------------TUPLE UNPACKING----------------------

#we can use * as the argument to a function to "unpack" values

def sum_of_all_nums2(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


nums = [1,2,3,4,5]
nums1 = (1,2,3,4,5)
print(sum_of_all_nums2(*nums))
print(sum_of_all_nums2(*nums1))








# #this dircelty passing the list to the function, will result in error
# print(sum_of_all_nums2(nums))
# #this syntax allows unpacking vlaues from a list
# print(sum_of_all_nums2(*nums))


#UNPACKING DICTIONARIES

def display_name(first, second):
    print(f"{first} says hello to {second}")

names = {"first":"Ali","second":"Khan"}
# print(display_name(names))

display_name(**names)  #dictionaries unpacking

def add_and_multiply_numbers(a,b,c):
    print( a+ b *c)

data = dict(a=1,b=2,c=3)
add_and_multiply_numbers(data)
add_and_multiply_numbers(**data)


