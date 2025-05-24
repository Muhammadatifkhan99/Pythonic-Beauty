# try:
#     file = open("/home/atif/Lab/Pythonic-Beauty/FileI/story.txt")
#     content = file.read()
#     print(content)
#     file.close()
# except FileNotFoundError:
#     print("The file 'story.txt' was not found.")


# file = open("/home/atif/Lab/Pythonic-Beauty/FileI/story.txt")
# print(file.read())

#file.seek(0) #sets the cursor to the start of the file



# f = open("/home/atif/Lab/Pythonic-Beauty/FileI/story.txt","w")
# f.write("Hello\n")
# f.write("World\n")

# print(f.read())

# f.seek(0) #set the cursor to the start of the file
# print(f.read())

with open("/home/atif/Lab/Pythonic-Beauty/FileI/story.txt","a") as f:
    f.write("We believe in concept\n")
    f.write("because all the great people were not toppers\n")




# print(f.closed)