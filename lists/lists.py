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
#the while loop allow us to have access to the loop counter variable while for does not
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

