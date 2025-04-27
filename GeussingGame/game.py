import random


random_number = random.randint(1,10)
x = None
while x != random_number:
    x = input("Enter a number: ")
    x = int(x)
    if int(x) > random_number:
        print("you are too high")
    elif x < random_number:
        print("You are too low")
    else:
        print("You won!!!!!!!!")
print(random_number)
    


# int(x) convert the number to integer, input() reads a number as a string