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
