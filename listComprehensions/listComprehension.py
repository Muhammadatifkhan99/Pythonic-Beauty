num = [1,2,3]

# print([x*10 for x in num])

#Looping 
numbers = [1,2,3,4,5]
doubled_numbers = []

for x in numbers:
    doub_number = x * 2 # doub_number = numbers * 2  --->this returns the list 5 times inside another list
    doubled_numbers.append(doub_number)

print(doubled_numbers)

numbers = [1,2,3,4,5]
doubled_numbers = [num * 2 for num in numbers]
print(doubled_numbers)


name = "atif"
print([c.upper() for c in name])
print([c.lower() for c in name])

friends = ['atif','ali','khan']
[f[0].upper() for f in friends]



#bool()

print([bool(val) for val in [0,[],'',12]]) #False, False, False


#converting a list of numbers to a list of strings

numbers = [1,2,3,4,5]

print([str(n) for n in numbers])

colors = ["red","orange","yellow","blue","indigo","violet"]
[color.upper() for color in colors]
#OUTPUT OF THE ABOVE CODE FROM INTERPRETER IS GIVE BELOW
#############################################################################################
# >>> colors = ["red","orange","yellow","blue","indigo","violet"]
# >>> [color.upper() for color in colors]
# ['RED', 'ORANGE', 'YELLOW', 'BLUE', 'INDIGO', 'VIOLET']
#############################################################################################





#################################################################################################################################################################################
#                                                               Conditional Logic in List Comprehension
#################################################################################################################################################################################


numbers = [1,2,3,4,5]


even = [num for num in numbers if num % 2 == 0]
print("The even numbers are: ",even)

odd = [num for num in numbers if num % 2 != 0]
print("The odd numbers are: ",odd)
################################################################################################################################################################################

with_vowels = "This is much fun!"
print(' '.join([char for char in with_vowels if char not in "aeiou"]))
########################################################################################################################################
#                                                               Nested List
########################################################################################################################################
#list inside of other list, multi dimensional list


nest_listed = [[1,2,3],[4,5,6],[7,8,9]]

print(nest_listed[1][1])
print(nest_listed[1][-1])

#using loop to print nested list

for n in nest_listed:
    for val in n:
        print(val)



board = [[n for n  in range(1,4)] for val in range(1,4)]
print(board)

print([["X" if num % 2 != 0 else "O" for num in range(1,4)] for val in range(1,4)])




