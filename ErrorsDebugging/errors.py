#ERRORS

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




#Try and Except Block

#strongly recommended to use try/except block to catch execeptions when we can do something about it.

try:
    foobar
except:
    print("problem")

print("after the problme")



# TRY/EXCEPT/ELSE/FINALLY BLOCKS OF CODE

# try: #try will try to do something
#     # num = int(input("Enter a number: "))
# except: #if there is a problem this runs
#     # print("Please enter a number")
# else: #if there is not a problem else will also run
#     # print("I'm the else block")
# finally: #finally will run no matter whats the problem
#     # print("No matter what I will run")



def dividby(a,b):
    try:
        return a/b
    except ZeroDivisionError as ZDe:
        print(ZDe)

print(dividby(1,2))
print(dividby(1,0))



