#SLICING IN PYTHON--> first_list[start:stop:step]

first_list = [1,2,3,4,5]

print(first_list[1:])
print(first_list[3:])
#incase of a negative index
print(first_list[-1:])
print(first_list[-3:])

color = ["red","orange","yellow","green","blue","indigo","violet"]
print(color[2])
print(color[2:])
print(color[0:])
print(color)
colors2 = color[:]
print(colors2)
print(colors2 == color)


print(color[0:2]) #the last index here is exclusive(not included in the result)

print(color[:-2])
print(color[:5])

lst = [1,2,3,4,5,6]

print(lst[::2])
print(lst[1::2])
print(lst[0::])

print(color[5][::-1]) #reverses the 5th value from the list


