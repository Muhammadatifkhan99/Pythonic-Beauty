# demo_list = [1,2,3,4,5,6,7,8,9]

# print(demo_list)
# print("The total elements inside the list are: ",len(demo_list))

#list() used to convert a range into a list or things like that

# r = range(1,10)
# print(r)

# print(list(r))

# print(list(range(1,11)))

# l1 = ["atif","ali","khan","sahal","umair"]

# l2 = [1,2,3,4,5,6]
#the while loop allow us to have access to the loop counter variable but the for loop does not
# i = 0;
# while i<len(l1):
#     print(f"{i}: {l1[i]}")
#     i += 1
#append adds one value to the list specified
# l1.append("lala")

# while i<len(l1):
#     print(f"{i}: {l1[i]}")
#     i += 1


#extend add all the values to the list
# l1.extend(["a","b","c","d"])

# while i<len(l1):
#     print(f"{i}: {l1[i]}")
#     i += 1


#inserting int a list values

# l1.insert(len(l1),"Muhammad")

# while i<len(l1):
#     print(f"{i}: {l1[i]}")
#     i += 1

#clear() removes everything from a list

# l1.clear()

# while i<len(l1):
#     print(f"{i}: {l1[i]}")
#     i += 1

# l1 = ["atif","ali","khan","sahal","umair"]


# print("The last element is popped up: ",l1.pop()) # removes the last element by default and if index was passed removes the element at the index.
# i = 0
# while i<len(l1):
#     print(f"{i}: {l1[i]}")
#     i += 1

# print(l1.index("sahal"))

# j = 0
# while j <= len(l1):
#     print(l1.index("sahal"))
#     j += 1;

# names = ["arya", "blue", "colt", "colt", "lena", "pablo", "selena"]
# print("I am friend with ".join(names))


first_list = [1,2,3,4]

print(first_list[3:])

print(first_list[::-1])
print(first_list[::-2])
print(first_list[0:2])
print(first_list[:])

string = "This is fun"
print(string[::-1])

numbers = [1,2,3,4,5,6,7,8,9]
print("Before: ",numbers)
numbers[1:3] = ["a","b","c"]

print("After: ",numbers)

names = ["James", "Michelle"]
print(names)

names[0], names[1] = names[1], names[0]

print(names)

#APPEND IN PYTHON---this add to the end of the list
#append takes in exactly one argument

data = [1,2,3,4]

print("List before the append applied",data)
data.append(5)
print("List after the append is applied",data)

data.append([5,6,7,8]) #this will append the entire list as one item to the list,the list will be couted as one item

#EXTEND IN PYTHON---adds to the end of a list all values passed to extend

first_list = [1,2,3,4]
print("before applying the extend",first_list)
first_list.extend([5,6,7,8])
print("after applying the extend",first_list)
print(first_list)

#extend and append add to the end of the list

#INSERT IN PYTHON --> insert an item at given position, where to insert is specified in index

another_list = [9,8,7,6]

another_list.insert(-1,"Hello") #inserts an element at the end of the list
another_list.insert(len(another_list),12)

print(another_list)


#CLEAR IN PYTHON--> remove all items from the list

first_lst = [1,2,3,4]
print(first_lst)
first_lst.clear()

print(first_lst)

#POP IN PYHTON-->remove the item at the give positon in the list and return it
#if no index is specified the last element is removed from the list.
l = [1,2,3,4]
l.pop()
print(l)
l.pop(1)
print(l)

#REMOVE IN PYTHON-->remove the first item from a list whose value is x
#throws a ValueError if the item is not found

j = [1,2,3,4,4,4]

j.remove(2)
# j.remove()
print(j)







#INDEX IN PYTHON-->returns the index of the specified item in the list
nums = [5,6,7,8,10]
print(nums.index(7)) #where 7 occurs in the list
print(nums.index(8,2)) #find 8 after the index of 2
print(nums.index(8,2,4)) #looking for 8 between the index of 2 and 4


#COUNT IN PYTHON--> returns the number of times x appears in the list
numbers = [1,2,3,4,3,2,1,4,10,2]
print(numbers.count(2))
print(numbers.count(21))
print(numbers.count(3))

#REVERSE IN PYTHON--> reverse the elements of the list (in-place: do not returns a new list but changes the older one)

lst = [1,2,3,4]
print(lst)
lst.reverse()
print(lst)

#SORT IN PYTHONG-->sort the element of the list(in-place)
k = [6,4,1,2,5]
k.sort()
print(k)

#JOIN IN PYTHON-->joins the data of the list together, its a string method
# the key idea is that its take a list and turn it into a string.
words = ["Coding","is","Fun"]

print(" ".join(words))