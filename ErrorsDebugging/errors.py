#ERRORS
from MakingHTTPRequest.dad import resutls


# 1. Syntax Errors

# def first:

# None = 1

# return 


# 2. Name Error :: Occurse when a variable is not defined

# Test 


#3. Type Error :: Operation or a function is applied to wrong type

# len(5)      #TypeError: object of type 'int' has no len()


# 4. IndexError :: happens when accessing something that does not exist or index that is out side the range of the list or string


# 5. ValueError :: This error occurs when a built in operation or function recieves an argument that has been the right type but now the right value.

# int ("foo")

# int (5) 



# 5. KeyError :: This error occurse with a dictionary when you try to access something from a dictionary but that key does not exist


# 6. Attribute Error:: occures when a variable does  not have an attribute




#####################################################333
########################################################
#### RAISING ERRORS IN THE CODE
##############################


##RAISE

# raise NameError("blah blah")

# raise KeyError("baak baak")


# def colorize(text,color):
#     if type(text) is not str or type(color) is not str:
#         raise TypeError("text and color must be strings")
#     if color not in ["red","green","blue"]:
#         raise ValueError("color must be one of red, green or blue")
#     print(f"{text} is {color}")
# colorize(12,13)



import pdb

first = "first"
second = "second"
pdb.set_trace()
result = first + second
third = "third"
result += third
print(result)

#import pdb; pdb.set_trace() commonly used on oneline

#common PDB Commands:
# p: print
# l: list
# n: next
# s: step
# c: continue
# q: quit

#if a variable name are same with pdb command use it like this, p and then the command so print and the command
