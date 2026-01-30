months = ("Jan","Feb","March","April")

for month in months:
    print(month)


#using a while loop to iterate on the tuple
i = len(months) - 1
while i >= 0:
    print(months[i])
    i -= 1


#Two Methods to work with on tuples

# 1. count()
# 2. index()

print(months.index("Jan"))

print(months.count("Feb")) #returns the number of times a value is in the tuple

#too-pul are used as keys in dictionaries
#tuple are immutable