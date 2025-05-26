# import csv

# with open("/home/atif/Lab/Pythonic-Beauty/CSV/fil.csv", mode='r') as file:
#     reader = csv.reader(file)
#     header = next(reader)  # Skip the header
#     for row in reader:
#         print(row)


# with open("/home/atif/Lab/Pythonic-Beauty/CSV/fil.csv", mode='r') as file:
#     dict_reader = csv.DictReader(file)
#     for row in dict_reader:
#         print(row)


from csv import writer, DictWriter

# with open("/home/atif/Lab/Pythonic-Beauty/CSV/fil.csv", mode='r') as file:
#     csv_reader = reader(file)
#     capitalNames = [[s.upper() for s in row] for row in csv_reader]
#     for row in csv_reader:
#         print(row)


# with open("/home/atif/Lab/Pythonic-Beauty/CSV/fil.csv", mode='a') as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(capitalNames)



with open("/home/atif/Lab/Pythonic-Beauty/CSV/file.csv", mode='w') as file:
    headers = ["Names","Breed","Age"]
    csv_writer = DictWriter(file, fieldnames = headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Names":"Kitty",
        "Breed": "Orange Tabby",
        "Age" : 10
    })
